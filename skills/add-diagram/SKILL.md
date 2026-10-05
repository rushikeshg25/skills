---
name: add-diagram
description: Add or improve an explanatory diagram in an existing Markdown or HTML document. Use only when the user invokes this skill or explicitly asks to add a diagram. Supports flows, sequences, states, relationships, and architecture; does not activate just because prose could benefit from a visual.
disable-model-invocation: true
metadata:
  author: rushikesh
---

# Add Diagram

Make a relationship or mechanism visible at the point where the reader needs it. Preserve the surrounding document and its conventions.

## Establish what the diagram must say

Read the target document and relevant evidence. Identify the question the diagram answers and the facts it must preserve: participants, direction, order, boundaries, branches, or state transitions. For code diagrams, trace the relevant implementation before drawing connections. Label assumptions and proposed behavior separately from observed behavior.

Infer the target and insertion point when clear. If several files are plausible, ask which one to edit before changing them. When the user asks for a new document or a snippet, deliver that form instead.

Choose the simplest useful visual:

| Reader's question | Useful form |
| --- | --- |
| Where does work or data go? | Flowchart with labelled edges |
| Who calls whom, and in what order? | Sequence diagram |
| What can change, and what triggers it? | State diagram |
| What belongs together or crosses a boundary? | Architecture or relationship diagram |
| How much, or how does a value change? | Chart with explicit units and sourced data |

Keep one main question per diagram. Split an overcrowded overview into an overview and a focused detail only when both help the reader.

## Match the document's renderer

- **Markdown with Mermaid support:** use a fenced `mermaid` block for flows, sequences, and states. Follow existing syntax and use stable, simple node identifiers with readable labels. Check support in the actual target renderer, not just a newer local Mermaid version.
- **Markdown without Mermaid support:** use a linked SVG asset with descriptive alt text when supported; use PNG if the target strips SVG. Keep the editable diagram source alongside generated assets. If rendering tools are unavailable, provide labelled source and state the rendering gap instead of leaving an unexplained code block.
- **HTML:** prefer inline SVG for precise relationships and layout. Reuse an existing diagram library when the page already has one. Provide an accessible name and a nearby textual explanation; keep SVG responsive without shrinking labels beyond readability.

Do not add a JavaScript dependency to a document just to draw a simple static diagram. A raster illustration can help explain a physical object, but exact labels, topology, and quantitative charts should use deterministic drawing tools.

## Integrate and check

Place the diagram next to the explanation it supports. Add a concise caption stating what it shows and define non-obvious notation. Use relative asset paths for portable documents. Preserve unrelated text, links, frontmatter, styles, and existing diagrams.

Check every node, edge, arrow direction, branch condition, and boundary against the evidence. Do not imply a sequence with arrows when the source establishes only an association. Use labels or shapes as well as color.

Render in the target environment when available. Inspect clipping, overlapping labels, reading order, contrast, and legibility at the document's expected width. For Mermaid, successful parsing is necessary but does not replace visual inspection. Check that Markdown fences close correctly, asset links resolve, and HTML remains valid after insertion.

Deliver the edited document with its required assets and name the inserted diagram. Report any unavailable renderer or unresolved factual assumption precisely. Do not claim visual verification if only source checks ran.
