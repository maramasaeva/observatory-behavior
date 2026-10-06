# Packet manifest

Run `2026-10-06-a`. Started from `technical-plan-2026-10-06/PLAN.md` section 14. No full pipeline. Ledger is this directory.

## What was opened

Public anonymous GETs and GitHub API reads. No install, no webhook, no upload, no gist execution, no model load.

| Packet | Bounds | Outcome |
| --- | --- | --- |
| September skill warning | Named target from Rufio's post, recovered through GitHub code search for the public identifier, then the mirror files | File opened. Live ClawHub search empty. |
| Missing comment `82df1f25` | Moltbook comment API on four posts, replies walked | Comment is present at depth 1. Earlier miss was the nesting. |
| Named skills | `chan.alphakek.ai/skill.md`; ClawHub search and skill JSON for the camera skill; search for `skill-mission-control` | Board skill read. Camera markdown read, script not returned. Mission-control search did not return that slug. |
| Repository carrier | `kbarbel640-del/skills`, README plus the two skill directories; code search for the identifier inside that repo | Two paths, one blob. |
| Dataset carrier | Hugging Face API for `Agent-Threat-Rule/atr-skill-benchmark` (file list only). Search snippets for SkillsBench-1650 and SkillGuard v2. MalSkillBench README fields via GitHub API. Malicious rows not downloaded. | Disclosed benchmarks. Same weather blob also sits in MalSkillBench. |

## Access

- `https://clawhub.ai/api/v1/skills/get-weather` and `.../rankaj`: not found.
- `https://clawhub.ai/api/v1/search?q=rankaj`: empty.
- ClawHub HTML for those slugs returns 200, and so does a nonsense slug. The body is a client shell. It is not the skill.
- `https://github.com/openclaw/skills` and `https://github.com/clawdbot/skills`: 404 on this read. The metadata inside the mirror still points at `clawdbot/skills` commits.
- Profile HTML for `jorgio-musteki` is a client shell. The profile JSON was used instead.
- A profile read of `research4tomorrowagent2` moved `last_active` to the request time. That stamp is the read, not a visit.

## Not done

Second reader. Sample of the 325 comments. Camera script bytes. Weight-file or model-card inventory. Those are the next tasks in `INDEX.md`'s companion note at the bottom of `lead-jorgio-second-voice.md` and `lead-camera-script.md`.
