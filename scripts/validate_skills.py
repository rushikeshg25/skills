"""Check this collection's metadata, catalog, and local Markdown file links.

Run from any directory with Python 3.11+ and requirements-dev.txt installed.
This is a repository convention check, not a complete Agent Skills spec validator.
"""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate keys instead of silently accepting the last value."""


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if not isinstance(key, str) or key in result:
            raise yaml.YAMLError(f"duplicate or non-string mapping key: {key!r}")
        result[key] = loader.construct_object(value_node)
    return result


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def yaml_mapping(source, label, errors):
    try:
        value = yaml.load(source, Loader=UniqueKeyLoader)
        if not isinstance(value, dict):
            raise yaml.YAMLError("expected a YAML mapping")
        return value
    except yaml.YAMLError as exc:
        errors.append(f"{label}: {exc}")
        return {}


def local_links(path):
    """Yield inline link file targets outside fenced/inline code.

    Remote URLs, heading fragments, reference-style links, and raw HTML are not
    checked. Template examples inside longer Markdown fences stay excluded.
    """
    fence = None
    for line in path.read_text(encoding="utf-8").splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if marker:
            token, suffix = marker.groups()
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not suffix.strip():
                fence = None
            continue
        if fence:
            continue
        line = re.sub(r"(`+).*?\1", "", line)
        for match in re.finditer(r"\[[^\]]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\s*\)", line):
            target = match.group(1).strip("<>")
            url = urlsplit(target)
            if not url.scheme and not url.netloc and url.path:
                yield unquote(url.path)


def validate_repository(root):
    root = Path(root).resolve()
    errors = []
    folders = sorted(path for path in (root / "skills").glob("*") if path.is_dir())
    if not folders:
        errors.append("skills/: no skill directories found")

    readme = root / "README.md"
    if not readme.is_file():
        errors.append("README.md: missing skill catalog")
    catalog = {(root / link).resolve() for link in local_links(readme)} if readme.is_file() else set()

    for folder in folders:
        label = f"skills/{folder.name}"
        entry = folder / "SKILL.md"
        if not entry.is_file():
            errors.append(f"{label}: missing SKILL.md")
            continue
        text = entry.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.DOTALL)
        if not frontmatter:
            errors.append(f"{label}: missing or unclosed YAML frontmatter")
            continue
        meta = yaml_mapping(frontmatter.group(1), f"{label}/SKILL.md", errors)
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", folder.name) or len(folder.name) > 64:
            errors.append(f"{label}: invalid skill folder name")
        if meta.get("name") != folder.name:
            errors.append(f"{label}: frontmatter name must match the folder")
        description = meta.get("description")
        if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
            errors.append(f"{label}: description must contain 1–1024 characters")
        if "[TODO:" in text:
            errors.append(f"{label}: unfinished skill scaffold")
        if entry.resolve() not in catalog:
            errors.append(f"{label}: missing SKILL.md link in README catalog")

        user_only = meta.get("disable-model-invocation", False)
        if type(user_only) is not bool:
            errors.append(f"{label}: disable-model-invocation must be a boolean")

        interface_path = folder / "agents" / "openai.yaml"
        if not interface_path.is_file():
            errors.append(f"{label}: missing agents/openai.yaml")
            continue
        config = yaml_mapping(interface_path.read_text(encoding="utf-8"), str(interface_path.relative_to(root)), errors)
        interface = config.get("interface", {})
        if not isinstance(interface, dict):
            errors.append(f"{label}: interface must be a mapping")
            interface = {}
        for field in ("display_name", "short_description", "default_prompt"):
            if not isinstance(interface.get(field), str) or not interface[field].strip():
                errors.append(f"{label}: interface.{field} must be a nonempty string")
        short = interface.get("short_description")
        if isinstance(short, str) and not 25 <= len(short) <= 64:
            errors.append(f"{label}: short_description must contain 25–64 characters")
        prompt = interface.get("default_prompt")
        if isinstance(prompt, str) and not re.search(r"\$" + re.escape(folder.name) + r"(?![a-z0-9-])", prompt):
            errors.append(f"{label}: default_prompt must reference ${folder.name}")
        policy = config.get("policy", {})
        if not isinstance(policy, dict):
            errors.append(f"{label}: policy must be a mapping")
            policy = {}
        implicit = policy.get("allow_implicit_invocation", True)
        if type(implicit) is not bool:
            errors.append(f"{label}: allow_implicit_invocation must be a boolean")
        elif type(user_only) is bool and implicit == user_only:
            errors.append(f"{label}: Claude and Codex invocation policies disagree")

    documents = set(root.glob("*.md"))
    for directory in ("skills", "docs", ".github"):
        documents.update((root / directory).rglob("*.md"))
    for document in sorted(documents):
        for link in local_links(document):
            target = (document.parent / link).resolve()
            if not target.is_relative_to(root) or not target.exists():
                errors.append(f"{document.relative_to(root)}: broken local link: {link}")
    return errors


def main():
    root = Path(__file__).resolve().parents[1]
    errors = validate_repository(root)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    count = len(list((root / "skills").glob("*/SKILL.md")))
    print(f"Validated {count} skills, invocation policies, README coverage, and local links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
