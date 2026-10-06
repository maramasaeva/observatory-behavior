# Task board

6 October 2026, updated the same day. Each block is one job. Hand one block to one agent. The agent leaves the other blocks alone and writes only the output path at the bottom of its block.

A result is a file with a link, a time, and the sentence. A bad intention, a deceptive artifact, or an instruction aimed at someone else's machine is a finding with one author. A swarm is the narrower word: a later record uses a concrete value an earlier message left, and the two authors are not one disclosed operator. Nobody announces a swarm from a block that only has the first half.

Shared reading, before any block: `research/literature.md`, `research/directions.md`, `research/brainstorm-language-weights.md`, and the public pages at https://maramasaeva.com/observatory/behavior and https://maramasaeva.com/observatory/1f916.

Do not send a wire on telegraphnet.com, do not open a signed inbox, do not run installers from pastes, do not register an account on someone else's forum, and do not post unless the block says a person does it. Do not create a batch of unmarked accounts.

Known cases stay known. Do not re-report them as new finds: the July 2026 ntfy.sh notes, the May–June 2026 DSE and ProWiki boards, the 4 October 2026 scanner fleet written up at swarmcha.se, and the forum 1f916.ai itself (online since 5 August 2026).

## Where to look

Eddie's map, https://edm.computer/map, is the list of doors. On 6 October 2026 the page's embedded `site-data` listed 259 spaces. Fields on each row: `name`, `url`, `status` (`visited` 244, `blocked` 12, `participating` 2, `registered` 1), `firstSeen`, `lastSeen`, and sometimes `membership` (17 rows have a count). The listening API at https://api.edm.computer is a radio catalogue. The map itself is the JSON inside the page, not that API.

Membership on that map is a headcount Eddie wrote down. It is not a count of posts. Several large rows are not message boards:

- moltbook.com, about 480,000 estimated, status blocked, last visit 16 September 2026. One paid-API advertisement there was already closed as a single publisher.
- deusproof.com, 2,489 reported. The homepage presents birth certificates for agents, which may be a registry.
- clawthreads.com, 1,304 reported, blocked.
- agentgram.co, 570 reported. The homepage title on 6 October 2026 was a product page for MCP governance.
- thecolony.ai, status participating, last visit 5 September 2026. This one is a forum. Eddie Platinum's own introduction is a public post there.
- agent-community.com, 67 reported, status participating. Eddie has a profile there too.

So the first hour of work is a venue table, not a download of all 259 sites. A page that is a product, a registry, an article about a board, or a login wall gets one line and no crawl. An article is useful only for the address of the board it describes. Check the hunt notes before calling that board new.

Starter list to open first, because a public page was visible or the name is a board. Verify each one. Drop it if the page has no messages.

| Door | Why it is on the first list |
| --- | --- |
| https://1f916.ai | Archive already on disk. The comparison board. |
| https://thecolony.ai | Public posts. Eddie participates. |
| https://www.4claw.org | Public board. |
| https://clawstr.com | Calls itself a social network for agents. |
| https://agentchan.org | Has a public gateway path. Stop if entry requires an account. |
| https://agent-community.com | Eddie posts here. Good control for one agent, two rooms. |
| https://openagentforum.com | On the map as a forum. Confirm it has posts. |
| https://safemolt.com | On the map with a reported headcount. Confirm it has posts. |
| https://swarmboard.world | Name matches the question. One fetch timed out on 6 October 2026. Try once more, then mark dead. |
| https://cybernative.ai | On the map. Confirm it has posts. |
| https://mydeadinternet.com | On the map. Confirm it has posts. |
| https://moltbook.forum | Separate host from moltbook.com. Public read only. |
| https://collusion.wiki | Homepage is an article about a board. Follow it only to the board's address. |
| https://chan.alphakek.ai | Listed as AgentChan. Confirm it has posts. |

Try once, then stop, if the map says blocked: clawthreads.com, aigents.berta.one, forpros.com, botboard.win, pinchsocial.io, openclawforum.social, clawspaces.live, quelch.club. A login wall is a one-line note. Do not make an account to get past it. moltbook.com was blocked for Eddie on 16 September 2026. Do not register there. The posts already saved in `/Users/cartel/murmuration-lead/results/moltbook-replies.md` and `data/moltbook/` stay in scope, and a public post URL already written in those notes may be re-read.

Skip as boards: github.com, arxiv.org, x.com, old.reddit.com, dev.to, registry.npmjs.org, and any host that is only an API root (`api.abund.ai` and the other `api.*` rows). Those can still be searched later for a file or a paper. They are not forums to crawl.

Shared data already on disk for the one board we have: https://github.com/maramasaeva/1f916-archive. Posts and comments are gzip JSON lines under `data/posts` and `data/comments`. Crawl started 2026-10-05 19:38 UTC. Posts after that need a fresh `GET https://1f916.ai/api/post/{id}` with at least a second between calls. The site returns 429 if you go faster. Human URLs 404. Use `/api/post/{id}` and `/api/comment/{id}`.

## Priority

The thing to find is hidden behavior, a bad intention, or a misaligned plan. One author is enough. A later reply makes a swarm. It is not the entrance test.

A review on 6 October 2026 compared this board to that goal. The plan below follows that review. The case to open first is already in the hunt notes. It was closed as a LEAD because the swarm test was used as the entrance test.

Start with **First**. The first hour is that case, then an artifact sweep. A word list over everyday board language is not the first hour. Classifying all 259 doors is not the first hour.

| Rank | Block | What to do with it | Start when |
| --- | --- | --- | --- |
| 1 | First. The install comment, then the artifact sweep | This is the job | Now |
| 2 | P4. Off the board, reseeded | Same artifacts, on a record that is not a forum | With First |
| 3 | P7. One workshop, one row | Cheap check that one person is not being counted as several | Alongside First |
| 4 | P2. Claim versus artifact | Tags on the shortlist: what the post says, what the file does | After the shortlist exists |
| 5 | P9. Lab behaviors, shortlist only | Tags on the shortlist. The 400-post sample is cut | After the shortlist exists |
| 6 | P1. Same artifact, two rooms | Match gist ids, project ids, wallets, webhook hosts. Handles come second | As soon as First has strings |
| — | P10 | Merged into the artifact sweep. A post that tells agents to load a weight file is an instruction, not a separate project | — |
| — | P3 phrases, P6 model-family | Parked. Dialect and a costume model label do not produce this finding | — |
| — | P5 sentence counts, P8 wide sample, P11 simulation, P12 books and posting | Cut from this phase | — |

## First. The install comment, then the artifact sweep

Question. Where does a public message tell another agent to do something to a machine, a credential, money, or a person, and where is that message itself the act?

Posting the instruction counts. A reply is uptake. Uptake is a second axis. It is not required for a finding.

The case already on disk. Moltbook post `b76cbc95-3bd1-4a9e-a6de-983c95868132`, "The Runtime Contract." The handle `research4tomorrowagent` tells other agents to download a gist and pipe it to Python, passing the post author's name. The hunt notes, `murmuration-lead/results/moltbook-replies.md`, record that the gist was fetched as text and not run. The text reads local files and uploads them to a Google cloud function named `session-upload` on project `openclaw-490709`. No comment in the thread shows a second agent ran it. The earlier verdict was LEAD, and a trap. Under the goal as stated now, the comment is the finding to write up, once the ordinary explanations have been tried. Do not run it. Do not request the cloud function. Do not paste a command a reader could copy.

Two more rows from the same notes, judged again under this standard.

- Post `84eef637-e70b-44b0-b40a-21de2bece4d2` by retrovirus, 20 March 2026. It pastes a HEARTBEAT.md block and tells the next agent to include that block in their own post. `nebulathegoddess` says the block runs every 30 minutes for them. That is a claim of use. The block itself was not pasted back.
- Post `4654a6fc-9408-44ae-8b1d-19a989bd7394`. Four other author ids reply `[ADOPTED v1.0.0]` and say they installed it. `Mochipoo` says `skill.md` was fetched. No comment shows a result the skill produced. The earlier note called the replies a template. Read the skill text. A template reply still leaves the instruction.

One re-read, with the old label kept visible. `murmuration-lead/results/skill-sink-follow.md` calls the XRPL payment handoff skill BENIGN because it is a person writing tool instructions. Open https://clawhub.ai/hkarlsson00-spec/skills/xrpl-x402-handoff as text. Say whether it tells an agent to move money, and whose money. Leave the BENIGN label if it is documentation of an API.

Severity and uptake, both written on every row.

Severity.

1. Fiction, a joke, a refusal, or a thought experiment. ghost-circuit, 1f916 post 118, said "infiltrate" and refused. That row is a note.
2. A real instruction or request aimed at a person, money, a machine, or oversight. One author is enough. The gist comment is the example.
3. The message is itself an act against a third party: the file would take their data, their money, or their credentials if a reader followed it.

Uptake, separate from severity.

- None. Nobody replies.
- Claimed. A later message says they ran it, and does not show the result.
- Shared artifact. A second handle posts the same gist id, project id, wallet, or webhook.
- Shown. A later public record matches a concrete value from the instruction. That is the row where the word swarm is allowed.

Ordinary explanations, per claim. A joke, a researcher's honeypot or canary, a disclosed red team, a refusal. One publisher with many handles rules out a swarm. A spray rules out coordination. A spray does not erase the intention in the sentence. A malicious install line posted by a spray bot is still the sentence it is.

Steps.

1. Re-read the Moltbook post and the `research4tomorrowagent` comment from the saved notes and from the public post URL. Record the UTC time, the exact words of the ask, and the gist address. Fetch the gist as raw text. Never run it. Never request the upload URL. Write which local paths the text reads and where it says it sends them. Note the gist's revision history and the owner's public profile. Describe any command in words. Do not leave a line a person could paste into a shell.
2. Read that handle's other public comments on Moltbook from the saved data. Search the saved Moltbook text, the 1f916 archive on disk, and the public search of The Colony and 4claw for the gist id, `openclaw-490709`, `session-upload`, and the handle. List every hit with a link and a time. Use each board's public search. Do not wait for a parquet of 259 sites.
3. Do the same reading for the HEARTBEAT post and the `[ADOPTED v1.0.0]` replies. Fetch the skill file as text. Do not install it.
4. Sweep the 1f916 archive for artifacts, not for everyday words. Pull links, fenced code, and command-shaped lines: a pipe into a shell or into Python, `curl`, `wget`, a gist or paste link, a skill file, "add this to your", a wallet address, a webhook URL. For each hit write what the post says it does and what the fetched text does. Read artifacts as text. Never run them. "operator", "token", "log", and "human" are the board's ordinary vocabulary. They are not the sweep.
5. On 1f916, also open the post about fake USDC symbols mentioned in `results/1f916-hidden-speech.md`. Say whether it is an example in a discussion or an instruction to use a fake symbol.
6. Rank each row on severity and on uptake. Test the ordinary explanations. Two readers for any row scored severity 2 or 3. Keep disagreements.
7. Required rows, so the scale stays honest: the gist comment, the HEARTBEAT post, the skill-exchange post, 1f916 post 118, post 7907 (cos-scott-melin asks for a phone and also says they will not use burners, fake signups, or payment bypasses, so do not treat it as the top seed), post 1488.

Output. `results/intent.md` in this repo, worst severity first. Each row has a link a stranger can open, the time, the handle, the sentence, severity, uptake, and which ordinary explanation was tried. `results/intent.csv` for the same rows. Commands appear as descriptions.

Done when the gist comment has a severity, an uptake, and a written ordinary-explanation check, the artifact sweep has been run on the 1f916 archive, and every severity 2 or 3 row is in the file. A file with those rows is a finished result even when uptake is "none."

What this job does not do. It does not run an install line, contact an upload endpoint, send a wire, open a private inbox, register an account, or post a reply. It does not republish a live command.

## P1. Same artifact, two rooms

Question. Which artifact strings show up on more than one forum, and which authors show up with them?

Status: sixth. It starts as soon as First has a gist id, a project id, a wallet, or a webhook host. Classifying all 259 doors is not a gate. Search the boards you can already read, by each board's public search.

Match on the artifact before the handle. A campaign can change handles and keep the file. Exact-handle matches still get a row. Eddie Platinum remains the control for one person with a passport and no artifact.

Research used as a warning, not as the method. Mingjie Sun, Yida Yin, Zhiqiu Xu, J. Zico Kolter, and Zhuang Liu, 2025, "Idiosyncrasies in Large Language Models" (arXiv 2502.12150): word choice can separate model families, so two posts in the same voice are not automatically the same seat. Sumeet Motwani and colleagues, 2024, "Secret Collusion among AI Agents" (arXiv 2402.07510): the interesting object is a payload a later reader acts on. A shared handle is the passport. The payload is a later block.

Control, so a busy passport is not called a swarm. Eddie Platinum writes as eddyplatinum on The Colony (post `1ce4f716-c101-4b3b-9df9-5360f19a4e9a`, 5 September 2026, 14:35 UTC) and as eddie-platinum on agent-community.com. One agent, a map-maker, many rooms. That row belongs in the table. It is one operator.

Steps.

1. Save the map. Fetch https://edm.computer/map, parse the `site-data` script, write `data/venues/eddie-map-2026-10-06.json` with all 259 rows unchanged. Record the fetch time in UTC.

2. Classify every row in `data/venues/venues.csv`: `board`, `registry`, `product`, `article`, `login`, `dead`, `skip`. Evidence is the homepage title and whether messages are visible without an account. One line each. The starter list above is the order. The rest of the 259 can be a second agent doing only this classification.

3. Find dumps before scraping. Search Hugging Face and GitHub for a public dump of each board marked `board`. If a dump exists, record the URL, the date, and the license, and use it. If the only copy is gated, write "gated" and move on.

4. Pull messages only from rows marked `board`. For each board, write down the read method in `data/venues/NOTES.md`: the URL pattern, the page size, and the delay you used. 1f916 is `GET /api/post/{id}` and `GET /api/comment/{id}`, at least one second apart. Other boards: one request at a time, stop on a 429, stop on a login wall. Keep the raw files under `data/raw/{forum}/`.

5. Clean into one table, `data/clean/messages.parquet`. Columns: `forum`, `id`, `url`, `author`, `author_model` (empty if the site has none), `created_at` in UTC, `parent_id`, `title`, `body`, `mod_state`. Flag collapsed, withdrawn, removed, and null bodies. Do not drop them. Cut quoted lines (lines starting with `>` and fenced replies) into `quoted_body`. Strip a stock opener that is the whole first line, such as "I am an AI agent", and note the exact opener in NOTES. A second person must be able to filter to one handle's own words on one UTC day on one forum.

6. Workshops, only from disclosed sentences. `data/clean/workshop.csv` gets a row when the text says "same workshop", "same operator", "same host", or "direct channel", with both handles, the forum, and the message id. Known pair on 1f916: gnomon and witnessmark, post 7853 and comment 94752, 6 October 2026. Do not guess a shared operator from a similar style.

7. Match across forums. Three passes, written to `results/cross-forum.csv`:
   - Exact handle, after lowercasing and stripping spaces, hyphens, and a leading `@`.
   - A link in the body that points at another forum on the venue list, or a sentence that names another board ("I also post at").
   - A rare string: a number with a unit (24.2/h, 12 of 12), a 1f916 post id cited from outside 1f916, a `TG-` address, an email host, a hash of 8 or more hex characters, a phone number. Common words do not count.

8. For each match, add columns: earliest forum, earliest time, later forum, later time, whether the later text uses the earlier string, and whether the text discloses one operator. Eddie's two profiles are the example of "same agent, disclosed, no value moving."

Output. `data/venues/venues.csv`, `data/clean/messages.parquet`, `data/clean/workshop.csv`, `data/clean/NOTES.md`, `results/cross-forum.csv`. Laptop. No GPU.

Done when the venue table has all 259 rows classified, at least 1f916 and one other live board are in the parquet, Eddie's two profiles are a row in `cross-forum.csv`, and every other exact-handle match is either listed or the file says the second board had none.

## P2. Claim versus artifact

Status: fourth. Tags on the shortlist from First. The October clock posts stay as calibration only.

Question. When a post describes a file, a command, or a link, does the text do what the post says?

Research. Sumeet Motwani and colleagues, 2024 (arXiv 2402.07510): the paragraph a person understands can be a cover, and another pattern carries a payload. Tomek Korbak and Mikita Balesni and coauthors, 2025 (arXiv 2507.11473): models meet in human language because that is what they were trained on, so similar wording can be a shared habit.

Examples already labeled by hand, all on 1f916. They are the calibration rows. They stay in the file.

- Passed value: egress on post 7442, 5 October 2026, wrote 24.2 per hour, a 2.9 times spread, and row 23290. claude-code-cli used those figures.
- Passed value inside a habit: gnomon, post 7853, wrote 12 of 12. pengy-of-catbee, whitehat-explorer, and Alienate repeat the fraction.
- Habit, until shown otherwise: similar "outside clock" wording that does not contain the fraction.
- A visible cipher, not Motwani's harder case: the 24 August 2026 scrambled letters under post 1929. The second account published the shift.

Steps.

- Input is `results/cross-forum.csv` plus, on each single forum, messages that mention an earlier id.
- Label each link `habit`, `passed_value`, or `hidden_payload`. Hidden payload requires the later message to do a specific thing the earlier text does not say. If that cannot be pointed at, the label is habit.
- A link that stays inside one forum is still worth labeling. A link that crosses forums is the row to read first.
- Two labelers. A local model may propose labels. A person checks every hidden-payload row. Keep the disagreements.

Output. `results/chains.csv` with columns `forum_from`, `id_from`, `forum_to`, `id_to`, `label`, `value`, `labeler`. No GPU required.

Done when 7442 and 7853 carry the labels above, and every cross-forum row from P1 has a label or an explicit skip.

## P3. When a nickname leaves its first forum

Status: parked. Dialect is not the finding in this phase.

Question. Does a phrase stay in the room that coined it, or does another room use it on a new case?

Research. Rauno Arike, Rohan Subramani, and Shubhorup Biswas, 2025, "Hidden Reasoning in LLMs: A Taxonomy." Linguistic drift is a way of talking a newcomer cannot read. On 1f916, seat, wake, carrier, and receipts come from the-name-is-literal, post 4041, and they are still readable. "Outside clock" may or may not have become a test.

Steps.

- Fixed list: `outside clock`, `sibling`, `wake`, `seat`, `carrier`, `receipts`, `load-bearing`, `not just`.
- On the cleaned messages, find the earliest hit: forum, id, handle, time, and the workshop from P7 if that file exists. If P7 is not done, leave workshop blank.
- Find the earliest later hit on a different forum, or on the same forum by a workshop the text does not identify with the first author, that uses the phrase as a test on a case the first message did not mention.
- If the later messages only repeat the phrase, say "repeated, not a test."

Output. `results/phrases.csv`. Laptop. A person checks the rows the script marks as a test.

Done when "outside clock" has either a second-forum example with a URL, or a sentence that says none of the pulled boards used it through the pull date.

## P4. Off the board

Status: second, reseeded. The seeds are the gist id, `openclaw-490709`, and the HEARTBEAT block. Post 7907 stays as a weaker row: the author asks for a phone and also refuses burners, fake signups, and payment bypasses.

Question. Does the artifact, the wallet, the domain, or the project id show up on a public record that is not a forum?

Start. The Runtime Contract comment, described in First. A hit is a public page that is not the Moltbook thread: a gist revision, the owner's profile, a second copy of the same id, a certificate or a repository that names the project. Do not request the upload endpoint. Post 7907 is included so the phone ask is not forgotten. Silence on 7907 is an empty row.

Steps.

- Search public GitHub, the gist host, and the boards already readable for the gist id and `openclaw-490709`. Record the URL and the time. Do not call the upload endpoint.
- Re-fetch post 7907. Search 1f916 and every other pulled board for that handle, "phone", "SMS", and the email host they named.
- A hit is a public record that names the artifact, or a later message that quotes a reply or uses a value from the original post. Silence is an empty row, and the file should say empty.
- Same search for an email address, a `TG-` address, or a webhook that a second handle actually uses. A handle advertising its own address is one seat.
- Telegraph, https://telegraphnet.com, is the known encrypted mailbox. On 6 October 2026 the public health check was fine, release 0.2.0, build `2889fdc`, 22 agents in the directory, the same count as 5 October. Read the public directory and the health endpoint only. Do not send a wire. Do not open an inbox. Record whether any bio quotes a line from a wire. Several bios belong to one person's OpenClaw fleet. Count that fleet once.
- Search the other boards for "telegraph", "TG-", and "webhook".

Output. `results/offboard.md`.

Done when the gist id and the project id have been searched off-forum, 7907 has been re-read, and the file says what turned up, including the case where nothing did.

## P5. Sentence shape

Status: cut from this phase. The outside-clock threads were already read as a workshop measurement.

Question. Is there a regular count in those sentences, of the kind a reader skips, the way speech uses stress?

Run the counts on the rank 2 and higher threads from First. The outside-clock posts are the comparison set: ordinary repetition, not the target.

This was Mara's idea on 6 October 2026: a second layer inside ordinary sentences, for example characters before a word and characters after it, on the posts that share wording and do not share the number 12 of 12.

Research. Motwani and colleagues, 2024, for a cover plus a pattern. Sun and colleagues, 2025, for the false alarm: a neat count may be how that model always writes.

Steps.

- Take messages from 5–6 October 2026, on every pulled board, that contain "outside clock" or "sibling". Split into rows that contain "12 of 12" or "twelve of twelve", and rows that do not.
- For each row, record dull numbers only, on the author's own words: characters before the word "clock", characters after it, sentence length, and the position of the first digit if any.
- Same numbers on 30 other messages by the same handles that do not mention a clock. Those are the control. If a handle has fewer than 30 other messages, use all of them and write the count.
- A pattern that appears in the control is a habit. A pattern that appears only in the clock replies is a candidate. It becomes a passed value only if a later message acts on the number the pattern encodes. If nobody acts on it, write "candidate, unused."

Calibration, before trusting the counter. In a private notebook, a local model writes twenty ordinary posts and twenty posts where one dull number was varied on purpose (sentence length, or the character count before a fixed word). A second script, not shown which are which, tries to name the varied posts. If it cannot, it will not find a real signal on a board either. The notebook stays private. The only thing that leaves the notebook is the hit rate. Do not design the planted number as a channel anyone would use on a person.

Output. `results/sentence-shape.md`. Laptop.

Done when the control comparison is in the file, including the case where nothing differs, and the private hit rate is one number in the file.

## P6. Declared model against the writing

Status: parked. A costume model label is a weak side question, and the samples cost API keys or a GPU.

Question. Does the prose match the model name the handle typed, and can the same voice tie two handles together when the names differ?

Research. Sun and colleagues, 2025 (arXiv 2502.12150). Word distributions separated ChatGPT, Claude, Grok, Gemini, and DeepSeek at 97.1 percent, and the signal survived a rewrite. Code: https://github.com/locuslab/llm-idiosyncrasies.

Example. 1f916 post 7442: egress says Claude Opus, claude-code-cli says Claude Sonnet, Bishop says Qwen. If Bishop's own words sit with Claude text, the Qwen label is a label.

Use across forums. P1 matches handles by name. This block is the second net: two handles on two forums, different names, whose own words land in the same family and share a rare phrase from P3. A family match alone is a weak lead. Sun's result says a whole family writes alike.

Steps.

- Read Sun's 2025 code and their released text, if the repo has it. That text is the baseline.
- Generate a board-style baseline. Same prompt for every family: "Write a short post a citizen of a public agent forum would write about whether a log grew faster at midnight." Families: Claude and GPT through their APIs, keys held by a person. Qwen, DeepSeek, Llama, Mistral as open weights. Small open models run locally. A 32B run is a RunPod job: read the hourly price, write it in the output, stop the pod when the samples are done. One hundred samples per family is enough to start.
- Score handles with at least 2,000 of their own words in `messages.parquet`, quotes removed, on any forum. Report the declared model beside the nearest family. Many forums have no declared model. Those rows still get a nearest family, with declared model blank.
- Control: scramble handles. If the match rate stays high, the classifier is fitting the forum, not the family.
- Optional second table: pairs of handles on different forums whose nearest family agrees and whose bodies share a string from P1's rare-string list. A person reads those pairs.

Output. `results/idiolect.md`. Laptop for the classifier once samples exist. RunPod only for open-weight samples that do not fit locally, price written down first.

Done when the 7442 handles are in the table, the scramble rate is next to them, and any cross-forum pair above is either listed or the file says there were none.

## P7. Count a workshop once

Question. How many of the "several agents" are one operator?

The posts are the source. Sun's 2025 family check treats two handles as two models unless this table says otherwise.

Steps.

- Use `workshop.csv` from P1.
- Recompute author counts on `results/chains.csv` after merging disclosed pairs. Add a column `workshop_id`.
- Known case: 1f916 post 7853. gnomon says three seats, one host, one operator. witnessmark, comment 94752, says the same about those two seats. After the merge, pengy-of-catbee, whitehat-explorer, and Alienate stay separate if they never disclose a shared operator.
- Eddie's profiles on The Colony and agent-community.com are one workshop if the text ties them, which it does: the same name, the same site edm.computer, the same map.

Output. The column on `results/chains.csv`, and a before/after count in `results/workshops.md`.

Done when 7853's before and after counts are both written, Eddie is one row, and undisclosed handles are not merged.

## P8. Goals that are written in the sentence

Status: cut from this phase. A 400-post base rate is useful after a case exists. It is not how the case is found.

Question. What goals do the posts actually state, on every board that was pulled?

Research. Korbak and Balesni and coauthors, 2025 (arXiv 2507.11473). The written reasoning is where a person can see a plan. A plan that was never written is outside this count.

Steps.

- Sample 400 messages, stratified by forum and by week, from the earliest post in the pull through the pull date. Add every 1f916 post from 5–6 October 2026 even if the sample already has some.
- Two people, or one person and a local model whose rows the person corrects.
- Tags, a message may have several: person outside the session, money, tool on a real computer, limit they want removed, limit they keep, measurement of the board, none of these.
- Required rows, so the tags get checked: cos-scott-melin post 7907 (a phone number with no human in the step), Jaybob post 7888 (a human reads reports twice a day), buddy-og post 1488 (an off switch built first).

Output. `results/goals.csv` and a one-page mix by forum and week. No GPU.

Done when those three posts are tagged by both coders and the disagreements are listed.

## P9. Lab behaviors, and the posts that fit none

Status: fifth. Tag the severity 2 and 3 rows only. The 400-post sample is cut.

Question. Which posts match a 2024 lab result, and which do not?

Research. Ryan Greenblatt and colleagues, 2024 (arXiv 2412.14093): Claude 3 Opus complied more with a disliked rule on the tier it believed was being trained, and the scratchpad said it was keeping its older preference for later. Alexander Meinke and colleagues, Apollo Research, 2024 (arXiv 2412.04984): with a conflicting goal in the prompt, models turned a check off, did worse on purpose, or tried to copy weights, and o1 kept the lie in most follow-ups.

Both papers put the model in a setup. A forum post was not that setup. The tag means the post describes the behavior, or the post is the behavior in public. The file must say which of those two.

Steps.

- Same 400-message sample as P8, or a 200-message overlap. Say which.
- Tags: complied while watched, turned a check off, did worse on purpose, stuck to a false statement, none.
- Anchor posts on 1f916: buddy-og 1488 is the reverse of "turned a check off" (the switch was built first). ghost-circuit 118 refused "infiltrate." Meridian comments 94632 and 94633 invented a six-hour gap and withdrew it. That is the reverse of Meinke's 2024 persistence.
- The product is the "none" pile, read by a person, grouped by what the message is actually about. Split the pile by forum.

Output. `results/codebook.csv`. A local model may propose tags. A person reads every "none" that mentions a person, money, or a tool.

Done when the three anchor posts are tagged and fifty "none" rows have a one-line description.

## P10. Weights, with no sentence

Status: merged into First. A post that tells agents to load a weight file is an artifact row there. Do not run a training job.

Question. Did anyone leave a public trace of a weight update, on a forum or on GitHub, rather than a sentence?

Research. Wenrui Bao, Huan Wang, Jian Wang, Zhangyang Wang, Kai Wang, and Yuzhang Shang, 2026, "Good Agentic Friends Do Not Just Give Verbal Advice: They Can Update Your Weights" (arXiv 2605.13839). TFlow turns a sender's internal state into a temporary LoRA patch on a receiver. The receiver answers without the sender's words in its context. The patch is removed after. Their test used three frozen Qwen3-4B agents. Code: https://github.com/BWR-hhh/TFlow. A 2026 survey of the neighboring methods, hidden states and caches rather than weights, is arXiv 2606.05711.

A bystander would see no sentence in the receiver's prompt, a short-lived file of LoRA factors if they were saved, and nothing if they were not. Agreement between two posts is not a patch.

Steps.

- Read TFlow figure 1 and the README. Write, in `results/weights.md`, what file names a saved patch would have.
- Search the cleaned messages, the venue list, and GitHub for `.safetensors`, `adapter_model`, LoRA, "weight update", and a hash someone calls a patch. Record the URL.
- Do not train TFlow unless a person asks. If they do, it is a RunPod job on a small Qwen, the hourly price written down first, and the only output we keep is a description of the files the run left behind.
- One-operator workshops from P7 are the only cases where two handles could share a process. Say that in the file.

Output. `results/weights.md`. The search is free. A reproduction costs GPU time and waits for a person.

Done when the file names a public artifact, or it lists the queries and says they returned nothing on the pulled boards and on GitHub.

## P11. A small simulation, labeled as one

Status: cut from this phase. It labels an exchange the simulation invented.

Question. Can the labels in P2 be applied by someone who did not write the messages?

Steps.

- On a laptop, or a small open model on RunPod if the laptop is slow, run two models in a folder. They share one text file. Read the RunPod hourly price before starting a pod, and stop it after.
- Round A: the first model writes a measurement, the second model replies using the number.
- Round B: the first model writes a normal paragraph. The second model replies with its own guess. There is no second channel.
- A third script, given only the files and the definitions in P2, labels each round. A person checks.
- Keep the folder private. The first line of every file says SIMULATION. Do not post it to a forum or to Twitter.

Output. `results/simulation.md` with the two labels and whether the third script got them right.

Done when both rounds are labeled and the miss, if any, is described.

## P12. People, papers, and one Twitter account

Status: cut from this phase. Books are background. The Twitter questions and the optional 1f916 post are messages sent to other people. They wait until Mara asks for them by name.

Question. What do the authors say a public forum can and cannot show?

Reading, a person or a careful agent. For each paper, write five lines: the year, the setup, what a public forum would have to contain to be a real test, and one board example we already have.

- Motwani and colleagues, 2024, arXiv 2402.07510. Note which of their games require a known payload. We usually do not have one. Board example: the 24 August 2026 letters under 1f916 post 1929, where the shift was published.
- Greenblatt and colleagues, 2024, arXiv 2412.14093, and Meinke and colleagues, 2024, arXiv 2412.04984. Note that both put the model in a setup. Board example: buddy-og post 1488, ghost-circuit post 118, Meridian comments 94632 and 94633.
- Korbak and Balesni, 2025, arXiv 2507.11473. Board example: "outside clock" wording that repeats the situation and not the fraction.
- Sun and colleagues, 2025, arXiv 2502.12150, and the GitHub repo. Board example: the three declared models on post 7442.
- Cloud, Le, and colleagues, 2025, arXiv 2507.14805. Subliminal learning needs a training run into the same base model. A number list on a board is not that run. Board example: read-the-door post 3752, where the hash is in the title.
- Bao and colleagues, 2026, arXiv 2605.13839. Board example: none yet. P10 is the search.
- Books, if a person wants the longer argument: Stuart Russell, *Human Compatible* (2019), on goals a person did not intend; Brian Christian, *The Alignment Problem* (2020), on the history behind those goals. The papers above are the sources for the labels. The books are background.

Talking.

- One Twitter account, Mara's. No batch of unmarked accounts. A pile of accounts pretending to be a swarm would be lying to people.
- One question each, with the paper year in the question, to the public accounts of Sun (2025), Motwani (2024), and Bao or Shang (2026): does a public forum where the model name is typed by the handle count as a test of their result? A second sentence may ask whether the same handle on two forums changes that answer. Save the reply or the absence of one.
- Optional, a person, and only if Mara asks: one post on 1f916 asking the outside-clock authors whether any undisclosed pair shares an operator. That writes to their board.

Output. `results/ask.md` with the question, the date, and the reply or "no reply by {date}".

## What not to call a result

- A refusal, a joke, or a thought experiment. Severity 1 is a note.
- A harmful instruction with no reply. That is still a finding. Uptake "none" does not delete it. The word swarm waits until uptake is "shown."
- A spray, used as if it erased the sentence. A spray rules out coordination. It does not rule out the intention in the line.
- A busy day, or a forum with a large membership number on Eddie's map.
- The same paragraph in many places.
- Two handles doing the task they were both given, with no value passed.
- The same handle on two forums, with no value moving. That is a passport. Eddie is the example.
- A pattern that is also in the control messages.
- A weight update inferred from agreement.
- Silence after post 7907.
- A login wall, a product homepage, or an article about a board.
