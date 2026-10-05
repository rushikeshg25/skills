# Video production decisions

Read this reference during production. Tool names are options, not dependencies guaranteed to exist in the host environment.

## Choose a rendering path

| Material and available environment | Practical choice |
| --- | --- |
| Geometry, equations, coordinate transformations; Python animation stack available | Manim or the existing mathematical renderer |
| UI, typography, diagrams; an established browser or React video pipeline | Existing browser renderer or Remotion setup |
| A small sequence of plots or diagram frames; Python and FFmpeg available | Deterministic SVG/PNG frames assembled with FFmpeg |

Reuse an existing project when one is supplied. Otherwise keep the production in a self-contained output directory. Use a project-local environment for needed dependencies and record versions; do not alter global packages just to render a clip. Check whether mathematical text needs a separate TeX installation before committing to that renderer.

A useful proof of the pipeline is one short clip containing the hardest visual, its text, and a sample audio segment if narration is required. This catches font, formula, codec, and timing problems before full production.

## Select narration deliberately

Use the user's chosen provider or supplied audio when available. For ElevenLabs or another hosted provider, inspect the current official API documentation before implementing calls. Read credentials from the configured secret mechanism or environment. Do not place keys in source, commands, logs, subtitles, or the delivered bundle.

The user's request to use their configured provider permits that requested use. If provider use or paid synthesis has not been authorized, prepare the script and render plan first, then ask before incurring charges or uploading private material. Do not request a key in chat; direct the user to the environment's secret configuration if required. Retry transient failures only within a small, explicit bound; stop on authorization or quota failures instead of switching to another paid provider.

For free or local narration, inspect installed options first. Examples include macOS `say`, an existing Piper setup, or another local TTS engine that fits the machine. Check voice quality, language, license, and model-download requirements. “Runs locally” does not mean “already installed,” “natural sounding,” or “licensed for every use.” Do not download a large model without accounting for its size and the user's constraints.

Generate a short sample before the full narration. Keep pronunciation adjustments in the spoken script; preserve correct notation in captions. If acceptable speech cannot be produced, offer a caption-led version or the precise setup needed. If narration was required, an unapproved silent substitute remains incomplete.

## Align sound and motion

Generate speech per scene and measure its actual duration with the available audio metadata tool, such as `ffprobe`. Word counts are planning estimates, not final timing. Define scene starts, visual events, and pauses in one timeline. Use that timeline for animation, audio placement, and captions to prevent drift.

Keep each formula or important result visible long enough to inspect. Place captions clear of key labels and respect frame margins. Use word timestamps when available; otherwise align caption segments to the measured audio and verify them by playback. Do not fabricate precise word timings from text alone.

Keep narration intelligible and free of clipping. Background music is optional and usually unnecessary for technical explanations. If used, ensure it is licensed and does not mask speech.

## Export and inspect

Use an export supported by the available encoder and the target player. H.264 video with `yuv420p` pixel format and AAC audio in MP4 is a common compatibility choice; keep dimensions even where the encoder requires it. A silent export has no required audio stream. Set the frame rate explicitly and use consistent frame geometry during assembly.

Inspect media metadata for duration, dimensions, frame rate, codecs, and expected streams. Confirm the full file decodes, then inspect representative frames at the start, important transformations, scene boundaries, and end. Play and listen to the export when tools permit. Metadata and still frames cannot establish that narration sounds correct or motion is smooth.

Check for missing glyphs, clipped equations, unexpected black frames, unreadable labels, abrupt cuts, frozen endings, truncated speech, and caption drift. Compare the final duration with the timeline. Report which checks actually ran and any inspection that the environment could not support.

Deliver only the needed outputs and reproducible source. Include a small production note with dependency versions, render command, asset attribution, and claim sources. Exclude credentials, caches, and temporary frame dumps.
