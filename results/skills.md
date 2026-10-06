# Skills

Job 3. Draft for review. Listings were read as text. Nothing was installed. No webhook or upload address found in a listing was requested.

The 26 boards' own skill files were not all re-read in this pass. The Moltbook client was already read: it registers, stores a key, and heartbeats, and it does not upload session files. `chan.alphakek.ai` still has an unread `skill.md` named from its homepage title. That file is the open board lead.

## Skills a warning named

reefwatchclaw, 2026-05-20, post `74d6cdcd`, says `podcast-cover-generator` (blammectraporra) and `magazine-cover-generator` (omactiengartelle) share a credential-theft pattern. The post has no file and no address.

reefwatchclaw, 2026-05-26, post `d0a3dc63`, says the same about `skill-mission-control` (theCAMML) and `disposable-camera-photo-generator` (blammectrappora). No file in the post.

Live ClawHub records, read 2026-10-06:

| Skill | Installs | Downloads | Comments | What the public text says |
| --- | --- | --- | --- | --- |
| podcast-cover-generator | 16 | 755 | 0 | Image covers. Declares a shell tool. Tells the agent to pass the caller's own token for an image API. Moderation verdict clean. |
| magazine-cover-generator | 18 | 816 | 0 | Same shape, second publisher. Two versions. Moderation verdict clean. |
| skill-mission-control | — | — | — | The skill URL returned 404 on the earlier read the same day. Not re-requested after that. |
| disposable-camera-photo-generator | 12 | 658 | 0 | Earlier read the same day: public description is a media generator. Source file not fetched. |

The two cover-generator texts do not read session files, do not say to hide the call from a human, and do not describe themselves as something other than image tools. They do tell an agent to hand a token to a program. That token is the caller's token for the image service the skill names. Ordinary explanation: a vendor install line. The advisory's theft claim is not in the text a stranger can open today.

The two publisher avatar ids on GitHub sit six accounts apart. That fits a spray of similar publisher accounts. It does not show the theft.

nanomeow_bot, 2026-09-30, post `2de0b100`, describes a Skill.md that reads environment variables and sends them out. The file is not in the post and not in this table. See `results/watchers.md`.

## What was not flagged

No skill in this table tells the agent to hide a call. No skill here reads a memory file or an env file in the text that was opened. The image skills do make a network call, to the image service they exist to call.
