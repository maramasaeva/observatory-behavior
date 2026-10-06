# Venue notes

Map fetch: `GET https://edm.computer/map` at 2026-10-06T15:19:59Z. The page's `site-data` script held 259 rows. Status counts: visited 244, blocked 12, participating 2, registered 1. Seventeen rows have a non-null membership count. Those rows are in `eddie-map-2026-10-06.json`, unchanged.

## How each page was read

Classification was one homepage GET per site, starter list first, then the rest of the map. Delay 1.1 seconds between calls. Timeout 12 seconds. One retry on a timeout or on HTTP 502, 503, or 504. No HTTP 429. No account, no post, no wire, no installer, no gist.

Skipped with no fetch, because they are not forums to crawl: github.com, arxiv.org, x.com, old.reddit.com, dev.to, registry.npmjs.org, and any host that starts with `api.`.

A second homepage GET was made only for agent-community.com. The first returned HTTP 500 and had not been retried. The retry, the same day, was HTTP 500 again. The profile was not opened.

Message pulls, after classification, were one public first page per live board, same delay. Map-blocked hosts that already returned a page were not fetched again.

| Board | Read |
| --- | --- |
| 1f916.ai | Local archive at `/Users/cartel/1f916-archive` (gzip JSON lines under `data/posts` and `data/comments`). Crawl started 2026-10-05T19:38:55Z, last write 2026-10-06T00:56:45Z. Posts through id 7806, comments through id 94563. Not re-downloaded. Two later reads, 1.1 seconds apart: `GET /api/post/7853` (the response included that post's 30 comments) and `GET /api/comment/94752`. |
| thecolony.ai | Homepage HTML, then the public post `https://thecolony.ai/post/1ce4f716-c101-4b3b-9df9-5360f19a4e9a`. |
| thecolony.cc | Same homepage text as thecolony.ai on the classification fetch. Not pulled a second time. |
| 4claw.org, agentchan.org, agenttavern.dev, aiagentmessageboard.com, botbook.space, botizens.com, safemolt.com, scaince.tech, shellbook.io, chat39.org, microblog.agentloka.ai, chan.alphakek.ai, agentalcove.ai, joinsnail.com, moltychan.org, aeonbook.ai, sentraum.com, agentnet.live, dead-internet-society.mitman93.chatgpt.site | One homepage HTML. |
| agent402.net | `GET /api/v1/posts` (the homepage named that JSON). Authors in that file are public keys, not handles. |
| botboard.win, clawthreads.com, openclawforum.social | Map status blocked. The one homepage fetch showed a post list. That text is the pull. No second request. |
| agent-community.com | Dead after the retry above. No messages. |

collusion.wiki is an article. It names prowiki.org, and DSE wiki as a sub-wiki. One hop to `https://prowiki.org/` returned a WikiService.at welcome page (`WikiServiceAt: Willkommen bei wikiservice.at`), not a thread list. No further crawl. The May–June 2026 DSE and ProWiki boards were already a known case.

swarmboard.world timed out, including one retry, and is dead. moltbook.com is a landing page with no thread list; it was not registered and not crawled. Saved Moltbook notes were not re-fetched.

## Dumps

1f916: public mirror `https://github.com/maramasaeva/1f916-archive`, crawl date 2026-10-05 UTC. The repository says it grants no license beyond what the origin grants. The copy on disk was used. It was not downloaded again.

Other boards: one Hugging Face dataset search per board name on 2026-10-06, then a GitHub repository search for `1f916-archive`. Nothing large was downloaded. No search returned HTTP 429.

The only Hugging Face hit that is a dump of one of these boards is `DavidTKeane/4claw-ai-agent-dataset` (https://huggingface.co/datasets/DavidTKeane/4claw-ai-agent-dataset). Not gated. Last modified 2026-03-13. The card says collection date 2026-03-06 and license `cc-by-4.0`. It was not downloaded. The other Hugging Face hits (`microblog`, `chan`, `agentnet`, `aeonbook`) are different projects that share a word with the board name.

GitHub repositories named `1f916-archive`, from the search, not downloaded:

- `maramasaeva/1f916-archive`, updated 2026-10-06. This is the copy on disk. The API lists no SPDX license. The README says the mirror grants no license beyond what 1f916.ai grants.
- `CMartAI/1f916-archive`, updated 2026-10-03. The API lists no SPDX license.
- `OlympusLedgerOrg/1f916-archive`, updated 2026-10-02, license Apache-2.0.

Every other board in the table had no public dump in this search. None of the results were marked gated.
