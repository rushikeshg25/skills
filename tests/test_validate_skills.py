"""Exercise validation outcomes on small, isolated repositories."""

from pathlib import Path
import tempfile
import unittest

from scripts.validate_skills import validate_repository


class SkillValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.skill = self.root / "skills" / "example"
        (self.skill / "agents").mkdir(parents=True)
        self.entry = self.skill / "SKILL.md"
        self.entry.write_text(
            "---\nname: example\ndescription: Explain an example.\n---\n# Example\n"
        )
        self.config = self.skill / "agents" / "openai.yaml"
        self.config.write_text(
            'interface:\n  display_name: "Example"\n'
            '  short_description: "Explain a concrete example clearly"\n'
            '  default_prompt: "Use $example to explain this."\n'
        )
        self.readme = self.root / "README.md"
        self.readme.write_text("[Example](skills/example/SKILL.md)\n")

    def assert_invalid(self, expected):
        errors = validate_repository(self.root)
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_model_invoked_skill_with_default_policy_passes(self):
        self.assertEqual(validate_repository(self.root), [])

    def test_user_only_requires_matching_harness_policies(self):
        self.entry.write_text(self.entry.read_text().replace(
            "name: example", "name: example\ndisable-model-invocation: true"
        ))
        self.assert_invalid("invocation policies disagree")
        self.config.write_text(self.config.read_text() + "policy:\n  allow_implicit_invocation: false\n")
        self.assertEqual(validate_repository(self.root), [])

    def test_rename_requires_metadata_prompt_and_catalog_updates(self):
        self.skill.rename(self.root / "skills" / "renamed")
        errors = "\n".join(validate_repository(self.root))
        for expected in ("name must match", "default_prompt must reference $renamed", "missing SKILL.md link", "broken local link"):
            self.assertIn(expected, errors)

    def test_duplicate_yaml_keys_are_rejected(self):
        self.entry.write_text(self.entry.read_text().replace("name: example", "name: wrong\nname: example"))
        self.assert_invalid("duplicate or non-string mapping key")

    def test_quoted_booleans_are_rejected(self):
        self.config.write_text(self.config.read_text() + 'policy:\n  allow_implicit_invocation: "false"\n')
        self.assert_invalid("must be a boolean")

    def test_malformed_frontmatter_is_reported(self):
        self.entry.write_text("---\nname: [\n---\n# Example\n")
        self.assert_invalid("expected")

    def test_nonmapping_interface_is_reported_without_crashing(self):
        self.config.write_text("interface: []\npolicy: false\n")
        self.assert_invalid("interface must be a mapping")
        self.assert_invalid("policy must be a mapping")

    def test_nested_example_fences_do_not_create_broken_links(self):
        asset = self.skill / "template.md"
        asset.write_text('````markdown\n# Template\n```python\npass\n```\n[example](future.md)\n````\n')
        self.assertEqual(validate_repository(self.root), [])
        asset.write_text(asset.read_text() + "[real link](missing.md)\n")
        self.assert_invalid("broken local link: missing.md")

    def test_relative_links_with_spaces_and_fragments_pass(self):
        reference = self.skill / "Reference Notes.md"
        reference.write_text("# Notes\n")
        self.entry.write_text(self.entry.read_text() + '[notes](<Reference Notes.md#notes>)\n[notes](Reference%20Notes.md)\n')
        self.assertEqual(validate_repository(self.root), [])

    def test_external_urls_and_example_inline_code_are_skipped(self):
        self.entry.write_text(self.entry.read_text() + '`[example](missing.md)`\n[site](https://example.com)\n[mail](mailto:user@example.com)\n')
        self.assertEqual(validate_repository(self.root), [])

    def test_missing_skill_entrypoint_is_reported(self):
        self.entry.unlink()
        self.assert_invalid("missing SKILL.md")

    def test_empty_repository_is_rejected(self):
        with tempfile.TemporaryDirectory() as empty:
            errors = "\n".join(validate_repository(empty))
            self.assertIn("no skill directories", errors)
            self.assertIn("missing skill catalog", errors)


if __name__ == "__main__":
    unittest.main()
