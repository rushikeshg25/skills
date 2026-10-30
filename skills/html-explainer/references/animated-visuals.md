# Optional animated charts and flowcharts

Read this reference when motion explains a change or the user requests it. The page must remain useful with animation off.

## Select a useful motion

- **Changing quantities:** transition existing marks to updated values after an input change. Keep series identity, units, and comparison scales stable. Explain any necessary rescaling. Show exact settled values; interpolated frames are not additional observations.
- **Time series:** use a labelled time cursor or a bounded playback sequence. Distinguish measured samples from interpolated or simulated values. Avoid smoothing that invents extrema or implies measurements between samples.
- **Process or flowchart:** keep the full topology visible and highlight the current node and traversed edge. Label branch conditions and show the selected path in text. Concurrent work must not appear sequential merely because nodes animate one at a time.
- **Before/after comparison:** preserve a reference state when it helps comparison. Do not move unrelated marks or reorder categories during a transition unless that change is the subject.

Prefer inline SVG with CSS or native animation APIs for small visuals. Reuse an existing library when it provides needed layout, scales, or interaction. For dense data, a chart library or canvas may be appropriate; supply a text summary or data table. Pin external library versions and disclose network requirements. Animation alone does not justify a new framework.

## Keep state and playback separate

Store the selected input, current step or time, and playback status explicitly. Derive labels, highlights, and values from that state. For step-through diagrams, define named steps with the active node, edge, and explanation instead of scattering independent timers through the page.

Start informative playback on a user action. Provide play/pause and replay; add step controls when the sequence teaches distinct stages. A brief input-driven chart transition needs no playback toolbar, but must settle promptly and work with motion disabled. Avoid endless loops.

Cancel or replace an in-flight transition when the input changes. Repeated play clicks must not create additional timers. Reset must stop playback, restore inputs and the initial state, and update text as well as graphics. Pause time-based playback when the page is hidden so returning does not skip unexplained steps.

## Accessibility and static output

Honor `prefers-reduced-motion` in both CSS and JavaScript, including changes while the page is open. With reduced motion, switch chart states immediately and let readers step through flow states without movement. Keep every state reachable.

Use native, keyboard-operable controls with visible focus and names that reflect their current action. Keep essential values and branch descriptions visible, not only in hover tooltips. Announce discrete user-selected steps when useful; do not send every animation frame to a live region.

Provide a complete static chart or flow overview before JavaScript runs. Printing should show a labelled, meaningful state and omit playback controls; never print an empty animation stage. Pair colors with labels, shapes, or line styles.

## Check the behavior

Inspect the saved page at wide and narrow widths and at browser zoom. Check:

- Initial, intermediate, and final values against the data or model; every branch against the stated process.
- Play, pause, resume, replay, step controls, and reset, where present.
- Rapid input changes and repeated play clicks; labels must match the final selected state.
- Reduced motion before load and during playback, keyboard operation, theme changes, and print output.
- Offline opening when the page is described as self-contained; report required external resources otherwise.

Record which checks actually ran. Source inspection alone does not verify animation or rendering.
