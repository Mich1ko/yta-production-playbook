# Production checks and repeatable operation

Keep reusable channel assets separate from episode assets. Use a structure such as channels/CHANNEL_ID/profile, characters, and environments; and episodes/EPISODE_ID/research, script, scenes, assets, edit, packaging, and review. Names are a convention and can be adapted to the tools in use.

| Checkpoint | Required evidence before moving on |
| --- | --- |
| Concept ready | Audience, question, payoff, evidence mode, and feasible production scope |
| Script ready | Complete spoken copy, source ledger, resolved story promises, timed reading |
| Visual plan ready | Original reference assets, complete shot coverage, coherent start and end states |
| Clips accepted | Actual duration and file known; identity, motion, framing, and continuity reviewed |
| Edit ready | Full runtime checked; narration complete; cuts, captions, color, and sound reviewed |
| Packaging ready | Three truthful candidates; script support; small-size readability; test hypothesis |
| Publication ready when requested | Final export, metadata, asset rights, applicable disclosure, and channel selection |

**Budget and retries:** estimate generation count from the shot plan, not just total runtime. Add image, audio, render, and regeneration costs when applicable. Use current quoted prices and keep estimated costs separate from actual charges. Record retry reasons. When the attempt or spending limit is reached, return the best accepted assets and a concrete simplification plan.

**Failure recovery:** missing reference files require recreating or obtaining references before dependent generation. A voiceover timing change requires updating scene times. A character redesign affects later scenes featuring that character. A title change may require a new hook, but it does not automatically invalidate every visual asset. Keep these dependencies explicit.

**Editorial value:** automation should support original stories, explanations, or commentary. YouTube's monetization guidance addresses repetitive or mass-produced material under its inauthentic content policy; using a reusable workflow does not establish that each resulting episode adds enough value. Evaluate the actual content. [S9]

**Disclosure:** assess the current requirements against the actual asset. YouTube's guidance distinguishes realistic synthetic or altered content from clearly unrealistic animation and ordinary production assistance. Do not automatically classify every animated video the same way. [S10]

**Learning loop:** store the chosen title, thumbnail, test outcome, relevant analytics, audience comments, and specific lessons. Revise the channel brief based on repeated evidence. Preserve uncertainty when samples are small. Do not turn one strong or weak upload into a universal rule.

# Sources and evidence notes

Research checked on 26 October 2026. Source titles and links below support the specific observations identified in the playbook. Operational recommendations and the worked pilot are original editorial guidance.

**S1  Supplied video**
ONE LAST TIME | An Animated Short Film, Day One Films. Title and channel checked through YouTube metadata; approximate visual and audio sequence inspected through automated video scene analysis. Full link: https://www.youtube.com/watch?v=f74QXnN2as4 . Requested starting point: https://www.youtube.com/watch?v=f74QXnN2as4&t=81s . Use the scene timings as approximate study notes, not a verified transcript.

**S2  Relatable second person opening**
TED-Ed, Why you procrastinate even when it feels bad. Official opening and lesson description support the analysis of starting with a recognizable situation. https://ed.ted.com/lessons/why-you-procrastinate-even-when-it-feels-bad

**S3  Counterfactual opening**
TED-Ed, What if every satellite suddenly disappeared, Moriba Jah. Official premise supports the analysis of introducing an altered condition and expanding its consequences. https://ed.ted.com/lessons/what-if-every-satellite-suddenly-disappeared-moriba-jah

**S4  Scenario and challenge opening**
TED-Ed, Can you solve the bridge riddle, Alex Gendler. Official opening supports the analysis of placing the viewer in an urgent fictional predicament. https://ed.ted.com/lessons/can-you-solve-the-bridge-riddle-alex-gendler

**S5  Titles and thumbnails**
YouTube Help, Thumbnail and title tips. Supports accuracy, concise wording, readable design, and evaluation by audience and traffic source. https://support.google.com/youtube/answer/12340300?hl=en

**S6  Audience retention**
YouTube Help, Measure key moments for audience retention. Supports reviewing the first 30 seconds and interpreting spikes and dips in context. https://support.google.com/youtube/answer/9314415?hl=en

**S7  Native testing**
YouTube Help, A/B test titles and thumbnails. Supports the up-to-three concurrent options, watch-time basis, eligibility checks, and possible inconclusive results. https://support.google.com/youtube/answer/16391400?hl=en

# Portable skill and further sources

**S8  Image to video prompting**
Runway Help, Image to Video Prompting Guide. Supports using the input image for appearance and composition while describing motion and camera behavior in the text prompt. Model capabilities must still be checked for the tool actually selected. https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide

**S9  Originality and monetization**
YouTube Help, YouTube channel monetization policies. Supports the distinction between original content and repetitive or mass-produced material addressed by the inauthentic content policy. https://support.google.com/youtube/answer/1311392

**S10  Synthetic content disclosure**
YouTube Help, Disclosing use of GenAI content. Supports evaluating whether realistic generated or altered content requires disclosure. Recheck the current guidance before publication. https://support.google.com/youtube/answer/14328491?hl=en

**R1 to R3  Supplied visual references**
R1 is Image 1, the dark emotional animation grid. R2 is Image 2, the illustrated survival scenario grid. R3 is Image 3, the saturated explainer grid. The original source screenshots informed the written reference analysis and are not distributed in this repository. Visible titles and performance counters are not independently verified factual or analytics evidence. Recreate the communication principles with original assets rather than publishing the screenshot designs as your own.

## Using the portable AI skill

The accompanying yta-production-playbook package contains SKILL.md, focused Markdown prompt references, the shared brief, the research notes, the worked pilot, and descriptions of the three supplied visual references. This repository distributes the Markdown skill; its linked files are the reusable production instructions.

For an assistant that supports skill folders, make the folder available through that assistant's normal skill mechanism. For another AI, attach or paste SKILL.md and the linked reference for the requested stage. A file can provide instructions and context; it does not train model weights or grant tools, account access, paid generation, or publishing authority.

**Example request:** “Use the YTA production playbook. Create a planning package for an eight-minute fictional survival video in English. Use second-person narration, an original illustrated protagonist, 16:9 framing, and an eight-second clip ceiling. Select a feasible idea, write the full script, prepare every image and motion prompt, and propose three thumbnail-title pairs. Deliver the plan and prompts.”

**To reuse one stage:** provide the completed brief and that stage's actual dependencies. Prompt 3 needs the locked script and visual references. Prompt 4 needs the story and packaging promise. Prompt 5 can run early on the idea and again on the finished script.

**To expand later:** connect real generation and editing tools, map the manifest fields to their supported inputs, add a budget limit and failure handling, and validate a short pilot before scaling the production volume.