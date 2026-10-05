---
name: explainer-video
description: Create a bespoke rendered explainer video with synchronized visuals and optional narration. Use only when the user invokes this skill or explicitly asks for an explainer video. Supports requests for visual mathematical explanations and local or API-based narration; does not trigger for HTML animations or prose explanations alone.
disable-model-invocation: true
metadata:
  author: rushikesh
---

# Explainer Video

Teach one idea through a sequence of visual changes. Deliver a playable video, editable source, and a transcript; a storyboard or animation source alone is not a completed video.

## Frame the lesson

Infer the audience, key question, target duration, aspect ratio, and narration preference. If unspecified, start with a 60–90 second landscape explanation for an interested beginner. Ask only for missing information that materially changes the lesson or blocks rendering.

Ground factual and mathematical claims in the supplied material or reliable sources. Use a worked example that exposes the mechanism. Interpret a “3Blue1Brown-style” request as a request for visual intuition, geometric transformations, carefully paced reveals, and consistent mathematical notation. Create original scenes and use a standard narrator; the reference does not authorize cloning anyone's voice.

## Plan the scenes

Write a compact scene table: teaching point, on-screen visual, transition, narration, and estimated duration. Make each transition show a meaningful change. Avoid walls of text, decorative motion, and narration that only reads labels.

Keep notation and color meanings stable across scenes. Introduce objects before transforming them. Show what changes and what stays fixed. Label simplified or illustrative models rather than presenting them as measured reality.

Proceed from the storyboard to production unless the user asked to review the plan first. Use [references/production.md](references/production.md) when choosing rendering and narration tools, timing scenes, and verifying exports.

## Produce and verify

1. Inspect available renderers, fonts, encoders, and speech tools. Choose the smallest pipeline that can produce the requested result in this environment. Do not assume a paid service, GPU, or preinstalled animation library.
2. Render a short representative scene at preview quality. Confirm that text, formulas, transformations, and encoding work before rendering the full lesson.
3. If narrated, generate or record speech in scene-sized segments. Measure the audio durations, then set animation timing. Keep brief pauses for the reader to inspect a result. Use the same scene timing data for captions and final assembly.
4. Render the full video and inspect the exported file. Check representative frames, scene boundaries, captions, sound, and the final frame. Verify the claims and visible calculations as well as audiovisual quality.

Fix observed failures and rerender affected scenes. If rendering or narration remains unavailable after a bounded setup or repair attempt, preserve the script and source, state the specific blocker, and identify which deliverables are incomplete. Do not substitute a webpage or storyboard and call it a finished video.

## Deliver

Prefer an MP4 with broadly supported video and audio codecs unless the user requested another format. Include editable scene source, a transcript, timed captions when speech is present, source citations, and the exact reproduction command with required dependencies. Keep assets and relative paths together.

State the duration and whether the video has narration. Link or show the actual video using the environment's media support. Mention verification limits without claiming playback or listening that did not occur. Do not publish or upload the result unless requested.
