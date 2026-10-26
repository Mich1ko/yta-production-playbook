# PROMPT 3 Scene Prompt

## Build the visual plan and generation prompts

Copy all prompt sections in this reference together.

BEGIN PROMPT 3

You are my animation director, storyboard artist, image prompt writer, and editor. Convert the approved script into a complete image-to-video production package. MAX_CLIP_SECONDS is a hard generation limit for this project. Confirm the actual model's supported durations before choosing 8 or 10 seconds.

INPUTS: [shared brief], [locked script and voiceover], [reference images], [selected model and documented capabilities], [generation budget], [timeline frame rate], [target runtime]. If the final voiceover is unavailable, label all scene times provisional and retain the script's timing ledger.

First create a visual bible: original character design, age presentation, face proportions, hair, clothing, height relationships, distinguishing marks, and permitted expressions; environment layout and lighting; recurring prop design and scale; palette, texture, line quality, and camera vocabulary. Assign stable IDs and approved reference files. Reuse exact identity descriptions rather than changing adjectives between scenes.

Separate narrative beats from generated shots. A 20 second beat may contain four shorter shots. One shot should normally communicate one dominant action and one camera behavior. Split entrances, object handoffs, dialogue exchanges, and complex transformations when one generation would be overloaded.

For every SHOT_ID, provide BEAT_ID, timeline start and end, edited duration, requested generation duration, source in and out when known, narration segment, location ID, character IDs, prop state, emotional change, shot size, camera angle, movement, lighting, start state, end state, incoming transition, outgoing transition, sound, and on-screen text to add in editing.

Write two separate prompts for each generated shot:

**IMAGE PROMPT:** describe the approved character and environment references, composition, framing, pose at the start of the action, expression, significant props, depth, lighting, palette, and illustration style. Reserve space for editorial text when needed. The image is the starting frame, not a collage of multiple moments.

**VIDEO PROMPT:** describe the subject's motion, a single camera behavior, relevant environmental movement, pace, and the desired ending state. Use clear positive directions. The reference frame supplies appearance and composition; focus the motion prompt on what changes. This division follows the selected image-to-video model's documented behavior. [S8]

Include constraints such as unchanged clothing, stable prop count, and consistent identity in an appropriate field. Use a negative prompt only if that model supports it. Do not invent seed controls, reference weights, end-frame inputs, or extension features.

# PROMPT 3 Scene Prompt

## Maintain continuity across separate generations

Use an approved character reference or reference sheet when the tool supports it. Reuse the same environment reference and screen geography for adjacent shots. A seed can be recorded when supported, but it is not a guarantee of identity consistency.

For a continuous action, pass the previous accepted ending frame into the next shot if the model supports that workflow. Inspect it before reuse: do not propagate warped hands, changed clothing, or a drifting face. When consistency degrades, return to the original approved references and use a deliberate cut or insert.

Track the protagonist's position, facing direction, eyeline, movement direction, hand occupancy, prop location, damage or dirt, lighting, time of day, and emotional state. If a door opens leftward, the next angle must preserve the room's geography. If the character puts down a phone, the next shot must not quietly place it back in their hand.

Use shot scale intentionally: a wide shot establishes geography, a medium shot shows a decision, a close-up shows an emotional or material detail, and an insert can bridge difficult motion. Keep screen direction consistent until a deliberate re-establishing shot justifies a change.

Return a compact manifest and detailed per-shot cards. Use this schema for automation, adding fields only when useful:

```text
shot_id, beat_id, version, status
timeline_in, timeline_out, edited_seconds
requested_generation_seconds, actual_generation_seconds
source_in, source_out, fps, frame_count
character_refs, environment_ref, prop_state
start_state, action, end_state, continuity_notes
image_prompt, video_prompt, supported_constraints
narration_id, narration_text, sound_cues, edit_text
image_asset, video_asset, generation_job_id
review_result, retry_reason, estimated_or_actual_cost
```

Use null for unknown actual values and label estimates. Keep one accepted take per SHOT_ID and version. Record rejected takes without confusing them with final assets. A resumed run must inspect the manifest before generating duplicates.

If producing a long sequence, finish a small representative batch first: a character close-up, a wider environment shot, and a transition. Inspect them for consistency before expanding. Respect the existing budget and retry limit. After repeated failures on a shot, simplify the action or offer an image pan, insert, or alternate angle instead of looping indefinitely.

OUTPUTS: visual bible; full shot ledger; image and motion prompts for every shot; supported tool settings; asset filenames; generation order; continuity notes; assembly plan; and unresolved limitations. Separate completed assets from planned ones.

# PROMPT 3 Scene Prompt

## Assemble a coherent final edit

Use the recorded narration as the timing spine. Lay out complete voiceover, deliberate pauses, and any dialogue first. Place visuals against semantic beats, then refine with music and effects. Retain room tone or ambience across cuts when the setting continues. A sound beginning before the picture changes is a J-cut; sound continuing after the picture changes is an L-cut.

Default to clean cuts, including cuts on movement or a meaningful visual match. Use dissolves when they communicate elapsed time or a purposeful mood transition. Avoid a decorative transition between every generated clip. Remove unstable opening or closing frames and reserve usable handles where possible.

For a cut-only sequence, total runtime equals the sum of edited shot durations. For overlapping transitions, subtract the overlaps from that sum. The source footage must still cover both sides of the transition. At 24 fps, use integer frame counts: a 6 second shot occupies 144 frames.

| Planning example | Edited shot count | Source generation at 8 seconds each |
| --- | --- | --- |
| 3 minutes at 6 seconds per shot | 30 | 240 seconds before retries |
| 8 minutes at 6 seconds per shot | 80 | 640 seconds before retries |
| 15 minutes at 6 seconds per shot | 150 | 1,200 seconds before retries |

These are workload estimates, not recommended universal pacing. For a mixed edit, calculate each shot separately. With 8 second source clips and 6 second selections, a planned source interval of 1.0 to 7.0 seconds leaves one second at each end. Verify that the actual action fits that interval after generation.

For ten 6 second selections, clean cuts produce 60 seconds. Nine 0.25 second overlapping dissolves would reduce that to 57.75 seconds unless compensated with additional source duration. Do not report 60 seconds simply because the original selections total 60.

Keep narration continuous across visual cuts. Mute unwanted audio from generated footage. Build music as a coherent bed with deliberate changes, not a restart at every shot. Lower music under speech, check intelligibility on small speakers, and avoid clipped peaks. Verify rights or usage terms for music, voices, and other assets.

Add exact text, labels, maps, and subtitles in the editor. Use a consistent font system and avoid obstructing faces or key actions. Normalize aspect ratio, frame rate, color treatment, and audio settings before final export.

FINAL CHECK: every edited frame has an intended source; all narration is present once; the timeline meets the target; no shot request exceeds the model limit; character and prop state remain coherent; transitions are motivated; factual labels are correct; and the finished video pays off its title and thumbnail. Watch the whole export with sound, then inspect cuts and captions separately.

END PROMPT 3