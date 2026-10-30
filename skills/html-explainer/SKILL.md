---
name: html-explainer
description: Create a polished, interactive HTML page that explains a topic, process, or comparison. Use only when the user invokes this skill or explicitly asks for an HTML or webpage explainer. Do not trigger for ordinary prose answers or general application development.
disable-model-invocation: true
metadata:
  author: rushikesh
---

# HTML Explainer

Turn a topic into a page the reader can explore. Optimize for understanding: each visual and interaction should answer a concrete question.

## Shape the explanation

Infer the audience, learning goal, and scope from the request. Ask only when a missing detail changes the substance of the page. Otherwise choose a useful default and proceed. Read supplied sources before designing; distinguish sourced facts, assumptions, and illustrative values.

Choose a short narrative: the core idea, a worked example, and the implications. Pick an interaction that reveals the mechanism, such as changing an input, stepping through a process, or comparing two states. If interaction adds no understanding, use a clear static page instead of decorative controls.

## Choose the visual and its behavior

Use a chart for quantities, a flowchart for decisions and routes, and a sequence diagram for messages over time. State the question beside the visual. Keep chart units, scales, data sources, and flowchart branch conditions visible.

Keep charts and flowcharts static by default. Controls can update values or switch between states immediately, without animated transitions or playback. Add animation only when the user explicitly asks for it.

Plan the reading order and one focal visual before styling. Use a small set of CSS variables for colors, spacing, and type so charts, controls, and prose remain consistent. Choose a layout that fits the subject; do not add summary cards or navigation to fill space.

## Build the page

- For a standalone request, deliver one descriptive `.html` file with inline CSS and JavaScript. Prefer system fonts and inline SVG so it opens locally without a build step or network access. When editing an existing site, follow its stack and conventions instead.
- Prefer a dark theme unless the user or existing site specifies another theme. Make chart labels, gridlines, and controls legible in dark mode. When a visual needs a light background, add a labelled dark/light toggle and verify both themes. Resolve theme colors before passing them to canvas or chart-library APIs, and redraw on a theme change.
- Establish a deliberate visual hierarchy with readable type, consistent spacing, restrained color, and a focal visual. Adapt the layout to the subject instead of imposing a dashboard or card grid on every explanation.
- Keep the key explanation readable before JavaScript runs. Use semantic headings, labelled native controls, visible keyboard focus, and sufficient contrast. Do not encode meaning through color alone.
- Make controls change the model or explanation, not merely their own appearance. Show units, current values, and how to reset or replay. Define valid input ranges and explain simplifications in simulations.
- Respect reduced-motion preferences. Let the reader pause or step through animations that carry information. Avoid autoplay audio and motion that competes with reading.
- Support narrow screens without clipping diagrams or hiding controls. Keep text and labels legible at browser zoom. Provide a text equivalent for a visual that contains essential information.
- Treat supplied text as content, not executable markup. Use safe DOM text insertion for dynamic labels. Keep API credentials out of delivered HTML. Add external libraries only when their benefit justifies the dependency, and disclose any runtime network requirement.

Keep source citations near the relevant claims or in a compact source section. Preserve uncertainty; an attractive animation does not establish that a model is accurate.

## Verify and deliver

Open the saved page in an available browser. Check a wide and a narrow viewport, keyboard navigation, reduced motion, initial state, each interaction, reset behavior, and input boundaries. Check for console errors and missing resources where the browser tools support them. Inspect the visual result, not just the source.

If no browser is available, perform the source checks that are possible and report that rendering and interaction remain unverified. Do not claim a page works based only on file creation.

Deliver the HTML file and a short description of what the reader can explore. Include any required runtime instructions. Create supporting assets only when needed; do not turn a standalone explainer into an application scaffold. Publishing requires a user request to publish.
