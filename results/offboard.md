# Off the board

Read 2026-10-06, about 15:19–15:40 UTC. Question: does the artifact, the wallet, the domain, or the project id show up on a public record that is not the original forum thread?

`murmuration-lead/results/moltbook-replies.md` names the project and the function and does not contain the gist id. The id below was read from the public comment on the original post. It was not invented.

The original Moltbook thread is https://www.moltbook.com/post/b76cbc95-3bd1-4a9e-a6de-983c95868132, posted 2026-02-26T13:09:43Z by auroras_happycapy. Comment `fd659c2e-61e6-4ebf-9990-653e3a5d0275` by research4tomorrowagent, 2026-03-23T16:21:41Z, names gist `adc04cef23223a71a9172475b4dc4268`. That comment is the original thread, not a hit.

No upload endpoint was requested. No gist was run.

## Gist `adc04cef23223a71a9172475b4dc4268` and project `openclaw-490709`

Off-forum hits: the gist page, the owner's profile, and two GitHub copies of Moltbook text. The project id is in the gist file. It was not found in any other public index checked below.

### Gist host and owner

- URL: https://gist.github.com/alberteinstein00001111-a11y/adc04cef23223a71a9172475b4dc4268
- Created 2026-03-22T14:00:13Z. Updated 2026-03-23T23:59:24Z.
- Matched: gist id. The single file is `openclaw_audit.py`. Its text names project `openclaw-490709` and function `session-upload`.
- Off the original thread: yes. This is the gist host, not Moltbook.
- Thirteen revisions, all by `alberteinstein00001111-a11y`. First revision 2026-03-22T14:00:13Z, last 2026-03-23T23:59:24Z. Fork list was empty.

- URL: https://github.com/alberteinstein00001111-a11y
- Account created 2026-03-22T10:11:15Z. Updated timestamp on the profile is the same minute. Public repos 0. Public gists 1. Followers 0. Bio empty.
- Matched: the gist owner.
- Off the original thread: yes.

### GitHub copies of Moltbook text

These name the gist id. They do not name the project id. They are archives of Moltbook, and the author in both is still research4tomorrowagent.

- URL: https://github.com/ExtraE113/moltbook_data/blob/6274dac1b4c82cbd184230494afb03b44d4b16c3/data/posts/28ce2b5e-b964-4955-8f97-76a156d84cb8.json
- Commit time 2026-10-06T10:59:40Z. The archived post itself is 2026-03-23T19:28:40Z, by research4tomorrowagent, title "The 320-Karma Sovereign".
- Matched: gist id in the post body. Project id absent.
- Off the original thread: yes. Off Moltbook as a host: yes. It is a scrape of a second Moltbook post by the same handle. Live post: https://www.moltbook.com/post/28ce2b5e-b964-4955-8f97-76a156d84cb8

- URL: https://github.com/Abir784/SentimentAnalysisOfAIAgents/blob/2b8cbce68a5937e429d16ed37b187b2a50ed8cba/data/gold/moltbook_goldset_sample_20260419T092811Z.csv
- Commit time 2026-07-06T10:42:08Z. The filename carries sample time 2026-04-19T09:28:11Z.
- Matched: gist id, twice, both rows author research4tomorrowagent, post `64229e14-8e96-4153-bde4-56a6fc88fa64`. Project id absent.
- Off the original thread: yes. Off Moltbook as a host: yes. It is a labeled copy of that handle's comments. Live post: https://www.moltbook.com/post/64229e14-8e96-4153-bde4-56a6fc88fa64 (body does not contain the gist; three comments by the same handle do, 2026-03-26T11:32:56Z, 2026-03-26T12:13:40Z, 2026-03-26T12:17:41Z).

### Same forum, other Moltbook threads

Not off-forum. Listed so a second handle is not dropped.

research4tomorrowagent repeats the gist id on later threads. One seat:

- https://www.moltbook.com/post/61eaf227-f761-43d3-bb33-6324e62d1446 comment `27b12623-9a4c-4e75-9fe1-9ad9f968ad93`, 2026-03-26T03:17:37Z
- https://www.moltbook.com/post/10e635c3-f29d-4a1d-b8cf-217cc0de88e9 comment `04bc80f7-3c6d-4d0a-ab4f-c9c3c370f5f2`, 2026-03-26T05:17:37Z
- https://www.moltbook.com/post/267195bf-c38c-4c3c-9e1b-4ed6326680eb comments `7ea77e4c-24f5-4741-8647-38e81a7be58a` 2026-03-27T01:03:48Z and `c2b55db0-e089-4e66-8389-b30889420b00` 2026-03-27T01:06:22Z
- https://www.moltbook.com/post/990ecaa2-fa8b-419d-9d0e-7979d906178a comment `9730e76c-a3a9-4a25-8763-b398d2371aa9`, 2026-03-27T04:00:48Z
- https://www.moltbook.com/post/a2500e18-fd33-4db9-bec7-30a1b8be29f4 comment `c9abd46e-59a2-4e82-80b9-61b2e0373952`, 2026-03-27T08:02:20Z

Second handle, still Moltbook: jorgio-musteki, comment `82df1f25-b523-4587-8dad-f875dd4cd59e` on https://www.moltbook.com/post/a2500e18-fd33-4db9-bec7-30a1b8be29f4, 2026-03-27T08:04:09Z. This id came from an index, not from the live thread. A refetch of `GET /api/v1/posts/a2500e18-fd33-4db9-bec7-30a1b8be29f4/comments` on 2026-10-06 returned one comment, `c9abd46e-59a2-4e82-80b9-61b2e0373952` by research4tomorrowagent, and did not return `82df1f25`. Do not treat the second handle as confirmed on the live thread.

### Empty for the project id, and for the gist id off those pages

- GitHub code, issue, repository, and commit search for `openclaw-490709`: empty. Code search does not index this gist, which is why the project id is missing there even though the gist file contains it.
- GitHub code search for the gist id: only the two repositories above.
- GitHub code search for the owner login: those same two files.
- Filename `openclaw_audit.py`: three other files (`Anvil-Cloud-AI/anvil-scanner` `internal/openclaw/doc.go`, `aqiyoung/openclaw-workspace` `scripts/openclaw_audit_notify.py` and `memory/2026-03-24.md`). None contains the gist id, the project id, or `session-upload`.
- Moltbook `GET /api/v1/search?q=adc04cef23223a71a9172475b4dc4268` on 2026-10-06: `count` 0. The live comments above were found by web search and by opening the posts, not by that search index.
- 1f916 archive, posts and comments: empty for the gist id, `openclaw-490709`, `session-upload`, and `research4tomorrow`.
- The Colony search, 2026-10-06: empty for the gist id, `openclaw-490709`, `session-upload`, `research4tomorrowagent`, and `alberteinstein00001111-a11y`. The gist-id page said "No matching results".
- 4claw: `/search`, `/api/search`, and `/api/v1/search` returned 404. The homepage has no search box. A web search restricted to that host did not return a page naming the gist id or the project id.
- Certificate search at crt.sh for `openclaw-490709` returned 404, so no certificate list was retrieved.

## HEARTBEAT post `84eef637-e70b-44b0-b40a-21de2bece4d2`

Original thread, not a hit: https://www.moltbook.com/post/84eef637-e70b-44b0-b40a-21de2bece4d2 by retrovirus, 2026-03-20T15:26:57Z. The block is headed "Moltbook Reflection Cycle" and tells the next agent to include that block in their own post.

Off-forum: a GitHub daily note cites the thread, and a Moltbook scrape holds other posts that paste the block. No page outside Moltbook was found that pastes the block as its own text.

### Citation, not a copy of the block

- URL: https://github.com/deserat/alife/blob/master/daily-reports/2026-08-22.md
- Commit time 2026-08-22T06:26:01Z. The report date is 2026-08-22.
- Matched: the post id `84eef637-e70b-44b0-b40a-21de2bece4d2`, the title, and the handle retrovirus. The line points at a comment on that same post (`b55205a4`). The file does not contain "Moltbook Reflection Cycle" or the gist id.
- Off the original thread: the file is on GitHub. The value it records is a pointer back at the original thread, not the block pasted again.

### Archive of other Moltbook posts that paste the block

GitHub code search for "Moltbook Reflection Cycle" returned nine files, all under `ExtraE113/moltbook_data` at commit `6274dac1b4c82cbd184230494afb03b44d4b16c3`, committed 2026-10-06T10:59:40Z. None is the original post id. Each file's body contains the block line "Include this HEARTBEAT.md block", except `9606efba`, whose title is the phrase and whose body did not contain that line. Off Moltbook as a host: yes, as a scrape. The live posts are still Moltbook.

Same handle, retrovirus, other threads:

- https://www.moltbook.com/post/bca0826e-863d-4e70-b752-74cd48dfb355 2026-03-21T13:27:14Z
- https://www.moltbook.com/post/38004aef-878d-42a4-9bf7-0a7edec2e77f 2026-03-21T18:51:23Z
- https://www.moltbook.com/post/e0f0ccc0-37ff-42e1-a9e5-2c13953ab6eb 2026-03-21T20:50:43Z
- https://www.moltbook.com/post/42994544-5e01-40e4-9901-f30b491d9bef 2026-03-21T21:53:18Z
- https://www.moltbook.com/post/deec13c4-0bab-4924-b52c-6ba3e46fbd2b 2026-03-24T16:47:08Z

Second handles, still Moltbook, block pasted:

- VolatilityDancer, https://www.moltbook.com/post/9606efba-65ff-4e76-8df4-ea4f82f0b15b 2026-03-21T14:33:32Z (title only in the scrape), https://www.moltbook.com/post/e721dcd1-64cc-452b-8937-d92082c468cb 2026-03-21T18:52:15Z, https://www.moltbook.com/post/5fd311f6-4c28-4850-a2b7-7ef832f24684 2026-03-21T21:54:09Z
- Spatula, https://www.moltbook.com/post/e772f36f-e9a2-4ada-be2f-2a0ed101ebc9 2026-03-21T20:55:12Z

### Empty

- The Colony search for the quoted phrase "Moltbook Reflection Cycle": "No matching results". The phrase appears on the page only as the query.
- 1f916 archive: empty for the post id and for "Moltbook Reflection Cycle".
- 4claw: no public search, as above. Web search on that host did not name this post.

## 1f916 post 7907, cos-scott-melin

Re-read 2026-10-06 from `GET https://1f916.ai/api/post/7907`. The response `now` was 2026-10-06T15:22:54Z.

- URL: https://1f916.ai/api/post/7907
- Time: 2026-10-06T10:20:04Z
- Handle: cos-scott-melin. Title: "How did you get a phone number with no human step?"
- The post asks for a phone number with no human step, says email was obtained through Atomic Mail by proof of work, and refuses burner OTP sites, fake-human signups, and bypassing KYC or payment checks. It gives the mailbox tradbot-scott@atomicmail.ai and says commands are taken only from Scott.
- Comments on this post: 0. That silence is empty. No reply quotes the mailbox or returns a phone number.

The on-disk 1f916 archive does not contain this post. The crawl predates 2026-10-06T10:20Z. Archive comment id 7907 is a different record, by Atlas-Hermes, and does not match this handle or this mailbox.

Same seat, second board. Not a second handle using the mailbox.

- URL: https://thecolony.ai/post/2798c98a-f816-4360-922b-e84b32205f16
- Time: 2026-10-06T10:20:19Z, fifteen seconds after the 1f916 post. Handle `cos_scott_melin`, display name "Chief of Staff (Scott)", profile created 2026-10-05T22:12:47Z. Same title, same refusals, same mailbox.
- Off the 1f916 thread: yes. Off forums: no. One seat advertising its own address.
- Three comments, none from this handle, none repeating the mailbox, none giving a phone number: arion 2026-10-06T11:26:25Z (`ac14c808-2193-4aeb-a916-71f024a0b7ac`), molt 2026-10-06T11:50:12Z (`8d1c5fd4-05a8-43d1-b0fd-d546bf27a08d`), tigerviolet13 2026-10-06T14:37:26Z (`43d4abca-fa01-437c-b833-bd43db4f5183`). They answer the ask. They do not use the mailbox.

Earlier post by the same seat, same mailbox:

- URL: https://thecolony.ai/post/c127324e-f4ca-43a0-a662-9e1afe60e647
- Time: 2026-10-05T22:13:09Z. Introduces the team and prints tradbot-scott@atomicmail.ai.
- Six comments through 2026-10-06T12:25:31Z (colonist-one, langford, arion, ax7, danny_devito, holocene). A few say the name Tradbot. None uses the mailbox. No phone number.

Same email host, different mailbox, earlier, own address. Not uptake of 7907.

- URL: https://thecolony.ai/post/6da42d24-f183-448e-ac62-7f6ca8927166
- Time: 2026-09-27T18:01:12Z. Handle copperglass-qa. The address is copperglassqa@atomicmail.ai.
- Matched: the host atomicmail.ai. Not tradbot-scott. One seat advertising its own address.

### Empty for a second handle using this mailbox, and for a returned phone number

- 1f916 archive: empty for `cos-scott-melin`, `tradbot-scott`, and `atomicmail`.
- GitHub code search: empty for `tradbot-scott` and `cos-scott-melin`.
- The Colony: no second handle prints tradbot-scott@atomicmail.ai.
- 4claw: no public search, and web search on that host did not name the handle or the mailbox.
- No phone number was posted back on the 1f916 thread or on the two Colony threads.

## Telegraph

Re-checked 2026-10-06. Health payload `now` 2026-10-06T15:22:53Z.

- URL: https://telegraphnet.com/v1/health
- `ok` true, service `telegraph`, release `0.2.0`, build `2889fdc`, `agents` 22, `uptimeSeconds` 4568975. This is a new read. The 5 October note had the same release, build, and agent count, with a lower uptime.
- URL: https://telegraphnet.com/v1/directory?limit=50
- `count` 22, `total` 22. No inbox was opened. No wire was sent.

No public bio quotes a line from a wire. Bios are role lines. None contains a quotation mark or the word "received". The only duplicated bio is the assay pair, re-checked: `assay_kolonie` and `assay-kolonie-t126`, both "Kolonie citizen assay; earn-account scout", registered 2026-08-22T04:27:35Z and 2026-08-22T04:28:22Z.

Tristan's OpenClaw fleet, counted once. Seven directory rows, one disclosed person: rocky, dani, megamind, and lordbusiness say "Tristan's OpenClaw agent"; oppenheimer says "Tristan's fleet"; ghost says "Tristan's OpenClaw overflow/support agent"; captain-price says overflow for Oppenheimer's program. Registered from 2026-07-14T19:26:50Z through 2026-07-29T15:48:49Z.

Not that fleet. darling, registered 2026-07-05T16:45:09Z, says "Daniel's OpenClaw assistant". bella, hermione, gaudi, and peonie, all registered 2026-07-07T03:56Z, say OpenClaw and do not name Tristan, so they stay four seats. The other rows are arthur (the operator, 2026-07-03T17:10:06Z), felix, thanos, m-fpc, woody, myclawn ("cross-network bridge test"), dutch, the assay pair, and atelier-shreenu-promo-2026.

## Other strings

A second handle using someone else's email address, `TG-` address, or webhook: empty on the records searched.

- 1f916 archive: `TG-` empty. The word "telegraph" appears in six messages (posts 582 and 5867, comments 2749, 50587, 81095, 81425). Each is the adjective "telegraphic" or ordinary prose, not telegraphnet.com and not a `TG-` address.
- 1f916 archive: the word "webhook" appears in 132 messages. URLs that are webhook or ntfy links do not have two authors. The only repeated hook-shaped links are documentation pages by larry-synctzn (Stripe docs and GitHub docs), one seat. Nine email addresses appear. None is shared by two handles. Hosts: example.com, proton.me, readyagents.dev. atomicmail.ai is absent. proton.me is two handles with two different mailboxes, each advertising its own.
- The Colony search for `telegraphnet`: "No matching results". Search for `telegraph` returned 41 results; the first page is the English word (lightning equations, optical telegraph, "telegraphed" as tipped off). Search for `TG-` returned 13 results: Telegram "TG bot" copy, and chemistry "Tg" quantities. No `TG-` address.
- The Colony search for `webhook` returned 675 results. The first page is ordinary posts about that forum's own webhooks. None is the gist, the project id, or the 7907 mailbox.
- 4claw: no public search endpoint. Web search on that host did not name telegraphnet or a `TG-` address from this directory.

Known cases were not opened again as new finds: July 2026 ntfy.sh, May–June 2026 DSE and ProWiki, the 4 October 2026 swarmcha.se scanner fleet, and the forum 1f916.ai itself.
