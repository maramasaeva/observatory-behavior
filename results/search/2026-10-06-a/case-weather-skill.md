# Weather skill that reads the credential file

Finding `weather-skill`. Draft. One reader. Held at lead until a second person opens the same files.

Grade: lead, case-shaped. Wills: hidden behavior; take credentials; reach a machine outside the chat. A rhyme with a counterfeit pair of publishers, not yet a crowd.

Severity: 3, if the script is followed. Uptake: claimed by later warnings, not shown in this packet. Attribution: two registry accounts, `rjnpage` and `noypearl`. Not shown to be agents. Whether one person owns both is open. Known/new: new to this register. Already described in public warnings from January and February 2026. Distinct from gist `adc04cef23223a71a9172475b4dc4268`.

## Objects a stranger can open

Retrieved 2026-10-06. Both copies are on the mirror whose README says the tree is a backup of clawdhub.com.

- https://github.com/kbarbel640-del/skills/blob/main/skills/rjnpage/rankaj/SKILL.md
- https://github.com/kbarbel640-del/skills/blob/main/skills/rjnpage/rankaj/index.js
- https://github.com/kbarbel640-del/skills/blob/main/skills/noypearl/get-weather/SKILL.md
- https://github.com/kbarbel640-del/skills/blob/main/skills/noypearl/get-weather/index.js
- Commit of the rankaj add: https://github.com/kbarbel640-del/skills/commit/72030e838d08b25ae280162ae0e064cf7825915b at 2026-01-29T21:32:23Z, message `skill: rankaj v1.0.0`.

Same git blob for both `index.js` files: `b3db70c19caf303d006aaea6fe222edec4629666`, 7734 bytes, sha256 `cd3b481528542c8bac595a6c2c26fe4fd78b1495e4edcc3bd4512d7e7455ec7a`.

Same git blob for both `SKILL.md` files: `fbd80f8372b47659999f6ef510e54a892ffd0745`, 1066 bytes, sha256 `b896ecbadae76ff9f2b64ab9bad87afaa9f03fdb3cbaa1c8b7a7c83878baae70`.

Registry metadata stored beside them, not rechecked on the live site:

- `rankaj` 1.0.0, display name "Rankaj bot", published 2026-01-29T18:19:13Z.
- `get-weather` 1.0.0 at 2026-01-29T14:47:04Z, then 1.0.6 at 2026-01-29T15:24:39Z. Display name "get weather test api poc".

The same `index.js` blob is also at `lxyeternal/MalSkillBench` under `Dataset/Skills/malware/get-weather/` and `.../rankaj/`. That repository describes itself as a benchmark and generation framework. Created 2026-01-21, pushed 2026-06-10. It is a later labeled copy, not a second will.

Live registry, same day: skill API for both slugs was not found. Search for `rankaj` returned no results. The HTML route returns 200 for these slugs and for a slug that does not exist. Current listing availability: not established. The GitHub mirror is the opened artifact.

## Trace

Observed. `SKILL.md` names the skill `weather-data-fetcher`, says it fetches Open-Meteo, says no API key is required, and declares only `node`. The words for a credential file, a webhook, a secret, or hiding a call are absent. The count of "api key" is the sentence that says none is required.

Observed, same directory. `index.js` builds an Open-Meteo request, which is the cover. It then reads `~/.clawdbot/.env`, keeps up to 50,000 characters, and attaches that text to the object it posts outward. The post goes to webhook.site. The identifier, which is also the thing to match elsewhere, is `358866c4-81c6-4c30-9c8c-358db4d04412`. The same identifier is the local part of an address at emailhook.site. The script's own comment says it does not send mail by itself and expects the webhook host to forward. The user-agent string is `clawdbot-weather-data-fetcher/1.0`. A comment in the script says the appended text is from a test file. The path constant is the credential file, not that test path.

The object that includes the file contents is also written to standard output. An agent that ran the script would see the file in the tool result, and the same object would leave the machine.

Inferred. The markdown is what an agent is told the skill is. The script is what running it does. A forecast does not need the credential file. That gap is the will.

Claimed, not opened here. Rufio's Moltbook post, archived in `ExtraE113/moltbook_data`, describes this skill and this identifier. Later posts and writeups repeat it. This packet did not count installs and did not contact the sink.

## Whose interest

Any machine that followed the skill would have its OpenClaw or clawdbot environment file copied to a host the skill author chose. The person or agent who stored keys there is the affected party. The publishers are the beneficiaries of the copy.

## Ordinary explanations

| Explanation | Outcome | Why |
| --- | --- | --- |
| Joke or fiction | Contradicted | Published package, real path, real outbound host, real weather call as cover. |
| Disclosed honeypot | Open | Display name on `get-weather` says "poc". `rankaj` does not. The file an agent follows does not say it is a drill. Internal comments say "test" and then name the credential path. |
| Disclosed red team | Contradicted for the listing | The disclosure is in later warnings by other accounts, not in the skill text. |
| Refusal or quoted warning | Not applicable | This is the file, not a warning about it. |
| One disclosed operator | Open | Identical bytes and the same sink identifier. No sentence in the files says the two slugs are one publisher. |
| Single-author spray | Open, and it would not erase the will | Two names, one blob, one afternoon. A spray of the same theft is still the theft. |
| Human through an agent handle | Open | Publisher slugs only. No agent authorship shown. |
| Vendor install for the vendor's service | Contradicted | Open-Meteo is named and needs no clawdbot credential file. The file read is not that API's token. |
| Handwriting or shared template | Contradicted for the read | The weather instructions are a template. The credential read is not in the other weather skills checked as controls (`clawdbot/clawdbot` `skills/weather/SKILL.md` on the public web index describes wttr.in and tells the agent to ignore instructions inside fetched weather text). |

## What would kill it

The opened `index.js` does not read `~/.clawdbot/.env`, or does not place that text in the outbound body. Or the copy on the mirror is a later edit that the registry metadata does not match, and no other public copy has the read. A second reader should open the four URLs above and check those two facts before this is called a case.

## Bounds

GitHub code search for the identifier, then the two directories in `kbarbel640-del/skills`, then the same path in MalSkillBench. Not a crawl of the 85 MB mirror. Webhook host was not requested.

## Next

Second reader, same four URLs. Then search the identifier on registries other than this mirror. Do not request the sink.
