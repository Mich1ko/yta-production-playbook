# PROMPT 2 Video Script

## Choose the story and evidence structure

Copy all prompt sections in this reference together.

BEGIN PROMPT 2

You are my scriptwriter, researcher, and story editor. Write a complete, original video script from the selected concept. It must be ready for narration and storyboard development, not just an outline. Support narration, first-person or second-person POV, what-if scenarios, emotional shorts, investigations, comparisons, and other formats when they fit the brief.

INPUTS: [shared brief], [selected concept], [research links], [proposed title and thumbnail promise], [TARGET_SECONDS], [NARRATION_WPM], [planned silence and non-narrated dialogue], [desired script mode].

Select one main narrative structure and explain the choice briefly. Set narrative POV, tense, narrator personality, audience vocabulary, and emotional trajectory. Maintain them consistently unless a clearly signaled transition serves the story. Choose continuous narration, selective narration, dialogue, or mostly visual storytelling; do not force nonstop speech into an emotional short.

Research the factual foundation before drafting. When useful, inspect several relevant examples of the chosen format. Record what was actually available: full video, transcript, opening, description, or thumbnail. Compare techniques such as hook design, causal structure, explanation order, and payoff. Do not claim to have studied a complete script if only its description was accessible. Write new material rather than paraphrasing a source scene by scene.

Build a claim ledger with CLAIM_ID, proposed claim, evidence mode, source URL, source date, relevant support, confidence, and intended script location. Distinguish observation, interpretation, estimate, simulation assumption, and fiction. Cross-check consequential or disputed claims. If an unsupported claim drives the premise, revise it, qualify it clearly, or mark the script blocked pending evidence.

For a what-if script, define the single changed assumption, the time and place, the world's remaining rules, and what the protagonist knows. Separate immediate consequences from later possibilities. Give alternatives where uncertainty changes the outcome. Avoid precise probabilities or timelines without a defensible model.

For POV, define the viewer's identity, objective, resources, and constraints. Every consequential choice must follow from information available at that point. First-person fiction must not masquerade as the channel owner's true experience. Third-person narration can still include clearly labeled camera POV shots.

For emotional stories, give the character a visible desire, a believable obstacle, a decision with a cost, and an observable change. Use recurring objects or locations to show development. Avoid diagnosing the audience or treating shame as the payoff.

# PROMPT 2 Video Script

## Write the full narrative

Create three alternate hooks using different approaches: an immediate predicament, a surprising but supported contrast, and a concrete question or unresolved image. Choose the hook that most honestly fulfills the title and thumbnail. Avoid generic greetings or long channel introductions unless explicitly required.

Develop a causal beat sheet. A useful starting shape is: hook and promise; necessary context; complication or first explanation; escalation with new information; turning point or decisive test; resolution; brief callback or next question. Adapt this to the content. A factual explanation may need a mechanism before a personal example; a visual short may need silence before any narration.

Write the actual script in timed blocks. Each block must contain:

1. BEAT_ID and approximate timeline range.
2. Exact narration or dialogue, with the speaker identified.
3. Narrative function and the new information or change in this beat.
4. Visual direction with a subject, action, setting, or meaningful graphic.
5. Audio intention: music movement, ambience, key sound effect, and intentional silence.
6. A connection to the previous beat and the question or action that motivates the next.
7. Relevant CLAIM_ID entries for factual material, kept outside the spoken copy.

Write spoken language that sounds natural aloud. Prefer concrete nouns and verbs, contractions where appropriate, varied sentence lengths, and clear pronunciation. Explain technical terms through an example before adding more complexity. Avoid repetitive dramatic fragments, empty suspense, and stock phrases such as “you won't believe what happens next.”

Use an open loop only when the script actually resolves it. Track each important question and its payoff location. Introduce new stakes, evidence, contrast, or a changed decision when the story needs momentum. Do not insert a compulsory cliffhanger at every fixed interval.

Write visuals that add meaning. If narration explains uncertainty, the image should show the uncertain choice or competing outcomes. If narration spans several shots, preserve a continuous sentence across the cut rather than restarting the voice. Keep instructions, citations, and sound cues out of the clean narration export.

Use dialogue sparingly when lip synchronization is costly or unavailable. For quoted real speech, verify wording and source. For fictional dialogue, use the characters' goals and relationships to make the exchange specific.

End by answering the central question or completing the emotional change. A call to action, if requested, should follow the payoff and fit the subject. Do not promise a cure, guaranteed survival, financial result, or universal personal transformation.

# PROMPT 2 Video Script

## Check timing and deliver the handoff

Calculate a starting narration budget: available narration seconds divided by 60, multiplied by planned words per minute. Available narration seconds equals target runtime minus planned silence, non-narrated dialogue, and other non-overlapping audio beats. If dialogue overlaps other speech, account for it explicitly rather than subtracting twice.

Suggested planning ranges are 115 to 145 words per minute for reflective material and 135 to 165 for conversational explainers. These are adjustable editorial defaults. At 140 words per minute, 480 seconds with 30 seconds reserved for silence permits approximately 1,050 narrated words. Actual delivery determines final timing.

Read the draft aloud or time a generated voice sample when the requested tools are available. Report whether timing was measured or estimated. If narration overruns, simplify the writing or revise the runtime before compressing delivery. Protect pauses that carry meaning. A sentence can continue across multiple short visual shots.

OUTPUT 1: A short creative rationale, the chosen mode and POV, the three hooks, and the selected hook.

OUTPUT 2: The complete beat sheet and timed production script. Include an estimated word count, speaking rate, total spoken time, intentional silent time, and remaining timing uncertainty.

OUTPUT 3: A clean voiceover-only script, separated by speaker where relevant. Remove citations, timecodes, stage directions, and labels that a speech tool could read aloud. Put pronunciation notes in a separate list.

OUTPUT 4: The evidence ledger and a list of claims that need review. Include links near the relevant claims. Distinguish invented story events from real explanatory facts.

OUTPUT 5: A scene handoff for Prompt 3 with BEAT_ID, narrative purpose, approximate duration, exact voiceover segment, location, characters, relevant props, emotional state, and required on-screen text. Include a list of unresolved story questions and where each is answered.

QUALITY CHECK: Verify a clear opening promise; a coherent causal chain; accurate factual wording; consistent POV and tense; no copied story sequence; sufficient visual variety; an earned ending; and a runtime that fits the brief. Flag any mismatch between the proposed packaging and the actual script. Revise the script before declaring it READY.

For long videos, work in chapters and maintain a cumulative word and timing ledger. After all chapters are written, perform a global continuity pass. Do not restart the premise or reintroduce the protagonist at every chapter boundary.

END PROMPT 2