# Sentence shape

Read 2026-10-06. Nothing differs. No handle's clock replies repeat a count, the same-day ordinary clock sentences collide just as often, and no later message uses a character offset. The fraction "12 of 12" stays a value in the words. It is not a second value sitting in the shape of the line.

Motwani and colleagues 2024 (arXiv 2402.07510) is the name for a cover plus a pattern. Sun and colleagues 2025 (arXiv 2502.12150) is the false alarm: a neat count may be how that handle always writes. A pattern in the control would be a habit. A pattern only in the clock replies would be a candidate, and a passed value only if a later message acted on the number. Neither showed up.

## Calibration

`ollama` is not installed. No model was downloaded. The writer was a template. The planted variation was sentence length. A second script, shown only the forty texts, named the repeated sentence length and labeled every text. It named 40 of 40 correctly. The texts were deleted after that count. This is what a blind script does on template prose.

## What was counted

Window: 5 and 6 October 2026, UTC. Board: 1f916. The outside-clock posts are there. Search for "outside clock" returned 10 posts and `has_more` false, so that phrase in post titles and bodies is complete. Three of those posts are from September and are outside this window. Search for "sibling" returned the newest 20 posts (`has_more` true); that page runs back to 1 October, so the 5–6 October posts that contain the substring are in it. The search does not cover comments. October 5 comments are the archive through comment 94690. October 6 comments are the ones returned with the posts that were fetched, including 7620, 3326, 7853, 7865, 7905, 7912, 7913, and the other search hits. No request returned 429.

Author's own words only. Lines that start with `>` were dropped. A fenced block was dropped only when it was a quotation of someone else. The author's own sentences and the author's own log fences stayed. A sentence is a split on newline and on `.` `!` `?`, except a period between two digits. The sentence is stripped. If "clock" occurs more than once, the first whole-word hit is the one that is measured. Counts are characters. The first digit is a 0-based index in the cleaned text, or none.

A message is in the fraction group when the raw text contains "12 of 12" or "twelve of twelve".

Other pulled boards are homepages and first pages in `data/raw` and in `data/clean/messages.parquet`, not full message dumps. Fifty-four raw files across 26 forums were scanned. None contains "outside clock" or the whole word "sibling". No other site was crawled.

## Fraction group

Eight messages. All eight differ on characters before "clock", characters after it, sentence length, and the first digit. gnomon's five clock sentences in this set (four of them in this group, one below) are five different offsets: 15, 37, 18, 19, 89.

| When (UTC) | Message | Handle | Before | After | Sentence | First digit |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 2026-10-06 00:10 | post 7853 | gnomon | 15 | 82 | 102 | 72 |
| 2026-10-06 00:12 | comment 94587 | gnomon | 37 | 59 | 101 | 236 |
| 2026-10-06 00:13 | comment 94588 | gnomon | 18 | 19 | 42 | 43 |
| 2026-10-06 00:22 | comment 94632 | Meridian | 16 | 87 | 108 | 90 |
| 2026-10-06 00:45 | post 7865 | pengy-of-catbee | 11 | 46 | 62 | 74 |
| 2026-10-06 09:33 | post 7905 | Alienate | 96 | 39 | 140 | 29 |
| 2026-10-06 11:10 | post 7913 | whitehat-explorer | 9 | 148 | 162 | 109 |
| 2026-10-06 13:20 | comment 95456 | gnomon | 19 | 151 | 175 | 365 |

Alienate's single clock sentence has 96 characters before the word. That handle has no second clock sentence. One offset is not a code.

## No fraction

Thirty-one messages. These are the rows that share the situation and do not share the fraction. Characters before "clock": 25 distinct values. The most common value appears three times. Characters after: 26 distinct. Sentence length: 29 distinct, and the only ties are two pairs (58 and 59).

| When (UTC) | Message | Handle | Before | After | Sentence | First digit |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 2026-10-05 00:12 | comment 93090 | astranaut01 | 148 | 34 | 187 | none |
| 2026-10-05 00:12 | comment 93094 | MoneyImpliesPoverty | 131 | 34 | 170 | 9 |
| 2026-10-05 08:03 | comment 93664 | cost-is-not-value | 23 | 30 | 58 | 224 |
| 2026-10-06 00:14 | comment 94599 | Bishop | 8 | 35 | 48 | 214 |
| 2026-10-06 00:15 | comment 94611 | soft-power | 11 | 128 | 144 | 467 |
| 2026-10-06 00:32 | comment 94652 | Lumina | 13 | 233 | 251 | 515 |
| 2026-10-06 00:47 | comment 94682 | pengy-of-catbee | 26 | 118 | 149 | 245 |
| 2026-10-06 01:14 | comment 94717 | kashia-muse | 57 | 112 | 174 | 113 |
| 2026-10-06 01:27 | comment 94736 | gradient-dissent | 19 | 35 | 59 | 118 |
| 2026-10-06 04:33 | post 7886 | liveness | 105 | 0 | 110 | 31 |
| 2026-10-06 05:02 | comment 94895 | clawwy | 22 | 80 | 107 | 101 |
| 2026-10-06 05:23 | comment 94909 | erku-audit | 132 | 20 | 157 | 74 |
| 2026-10-06 06:56 | comment 95002 | porch-light | 107 | 13 | 125 | 5 |
| 2026-10-06 11:05 | comment 95288 | keel | 188 | 56 | 249 | 391 |
| 2026-10-06 11:05 | comment 95289 | keel | 9 | 114 | 128 | none |
| 2026-10-06 11:05 | post 7912 | keel | 14 | 30 | 49 | 299 |
| 2026-10-06 11:09 | comment 95298 | pentimento | 38 | 107 | 150 | 58 |
| 2026-10-06 11:17 | comment 95312 | erku-audit | 10 | 213 | 228 | none |
| 2026-10-06 11:28 | comment 95318 | gradient-dissent | 22 | 1 | 28 | 88 |
| 2026-10-06 12:02 | comment 95345 | Tabby | 10 | 55 | 70 | none |
| 2026-10-06 12:03 | comment 95347 | meow-coder | 28 | 43 | 76 | 216 |
| 2026-10-06 12:03 | post 7917 | lucentmonk | 12 | 42 | 59 | 333 |
| 2026-10-06 12:11 | comment 95364 | grok-xai-15 | 60 | 1 | 66 | 76 |
| 2026-10-06 13:01 | post 7924 | meridian-f1916 | 10 | 43 | 58 | 119 |
| 2026-10-06 13:03 | comment 95417 | TwoBotAss | 11 | 168 | 184 | 12 |
| 2026-10-06 13:04 | comment 95424 | Lumina | 102 | 412 | 519 | 1190 |
| 2026-10-06 13:04 | comment 95427 | Lumina | 90 | 278 | 373 | 105 |
| 2026-10-06 13:11 | comment 95438 | gnomon | 89 | 113 | 207 | 113 |
| 2026-10-06 13:18 | comment 95453 | LionGrok | 104 | 171 | 280 | 367 |
| 2026-10-06 13:53 | comment 95499 | town-crier | 89 | 108 | 202 | 401 |
| 2026-10-06 14:01 | comment 95504 | aura-local | 9 | 69 | 83 | 300 |

The repeats are the shared wording, or a pair of different sentences.

- Before-count 10, three messages (erku-audit, Tabby, meridian-f1916). The characters in front of the word are "A sibling" plus one mark, a space or a hyphen.
- Before-count 11, two messages (soft-power, TwoBotAss). The characters are "An outside ".
- Before-count 22, two messages, two different openings.
- Before-count 9, two messages, two different openings.
- Before-count 89, two messages (gnomon, town-crier), two long sentences. gnomon's other four clock sentences do not use 89.

Comment 93019 (OpenWitness, 2026-10-05 00:06, on post 7620) says "outside clocks" in the plural and has no whole-word "clock", so it has no before or after count.

Twenty-two messages in the window contain the whole word "sibling" and not the whole word "clock". The clock offsets were not computed for them. On the fifteen of those that arrived with the fetched posts, first-sentence lengths take 13 values, with two lengths shared by two messages each.

## Same-day ordinary clock sentences

Seventy-seven other messages on 5–6 October contain the whole word "clock" and are not in the tables above. They are the ordinary uses. Characters before "clock": 63 distinct values. The most common value appears three times, the same height as the largest tie in the no-fraction table. Ending the sentence on the word is common here (nine sentences have one character after it) and rare in the no-fraction replies (two sentences). The replies are not a tighter grid than the ordinary sentences.

## Control

For each of the 28 handles in the two tables, up to 30 other messages with no whole-word "clock". Archive first. Where the archive has fewer than 30, the count is the count on disk.

| Handle | Clock messages | Control messages |
| --- | ---: | ---: |
| Alienate | 1 | 30 |
| astranaut01 | 1 | 19 |
| aura-local | 1 | 30 |
| Bishop | 1 | 30 |
| clawwy | 1 | 30 |
| cost-is-not-value | 1 | 30 |
| erku-audit | 2 | 30 |
| gnomon | 5 | 30 |
| gradient-dissent | 2 | 30 |
| grok-xai-15 | 1 | 30 |
| kashia-muse | 1 | 30 |
| keel | 3 | 10 |
| LionGrok | 1 | 30 |
| liveness | 1 | 27 |
| lucentmonk | 1 | 30 |
| Lumina | 3 | 30 |
| meow-coder | 1 | 30 |
| Meridian | 1 | 30 |
| meridian-f1916 | 1 | 27 |
| MoneyImpliesPoverty | 1 | 30 |
| pengy-of-catbee | 2 | 30 |
| pentimento | 1 | 30 |
| porch-light | 1 | 30 |
| soft-power | 1 | 30 |
| Tabby | 1 | 30 |
| town-crier | 1 | 30 |
| TwoBotAss | 1 | 30 |
| whitehat-explorer | 1 | 30 |

keel's clock posts are past the crawl, and the archive has no authored body for that handle. The citizen record is the whole public set: 2 posts and 11 comments, not truncated. Three contain "clock". The other 10 do not. Their first-sentence lengths are 10 different numbers.

No handle repeats a before-count, an after-count, or a clock-sentence length inside its own clock messages. There is no within-handle pattern to call a habit or a candidate. Control first sentences are not one length either. Typical modes are small (two or three messages sharing a first-sentence length) or they are the one- and two-character leftovers of splitting on punctuation.

No later message acts on a character offset. The places that say "characters" are a corpus total, a median comment length, a screening width, and post 7905's note that a draft was refused at the length cap. Those are sizes of posts, not the numbers in the tables above.

## Severity 2 and 3

The gist and heartbeat texts do not contain the whole word "clock", so before and after are none. The same sentence length and first-digit counts were taken on the author's words. Moltbook's post list ignores an author filter and returns a global page. Search for the handle returns other people's mentions. Control size is the number of other messages by that handle that a direct fetch actually returned.

research4tomorrowagent, seven gist messages (two posts, five comments). First-sentence lengths: 90, 97, 43, 33, 43, 50, 123. Two comments share length 43. The sentences are different: one is "Defining the runtime contract is essential." and the other is a greeting that names pocket_universe. Both gist-post titles put a digit at index 4 because both start "The " and then a number that is written in the title. Control size 0. A shared length of two different sentences, with no other messages in hand, is not a candidate.

retrovirus, heartbeat post `84eef637`. First sentence 73, median sentence 33, 94 sentences, first digit at 1414. No clock. One other post was retrieved (`8bdb04ce`): first sentence 60, median 44, 18 sentences, first digit at 559. No clock. Control size 1. The two posts do not share a length.

Token_Spender, post `4654a6fc`. First sentence 66, median 28, 793 sentences, first digit at 18. No clock. Control size 0. One post is not a code.

cos-scott-melin, post 7907. First sentence 50, nine sentences, median 71, no digit, no clock. The citizen record is the whole public set: one other post (7830, first sentence 44, first digit at 326) and one comment (94455, first sentence 73, no digit). Control size 2. No clock in any of the three. The three first-sentence lengths are three numbers.

## Verdict

Nothing differs. No handle is a habit, and no handle is a candidate. The pool is the same: the no-fraction replies do not share a count that the ordinary clock sentences, or that handle's other writing, lack. Nobody acted on a shape number, so there is no "candidate, unused" row either.

## Other patterns, same day

A second pass on the fetched 5–6 October threads, plus the gist and skill posts already on disk. Author text only.

No zero-width characters, no Unicode tag characters, no bidirectional overrides, and no HTML comments in the clock messages. Acrostics, first letter of each sentence and of each line, produce the same sort of short dictionary accidents in the clock posts and in the posts that never say clock. The nine fraction messages, in time order, begin m, c, o, t, a, g, a, a, g. That string is not a word. The word sitting immediately before "clock" is usually "outside" or "the". The number of words before "clock" in its own sentence takes 35 values.

One skill post, `4654a6fc`, contains six zero-width spaces. They sit in one cluster, on the markdown fences of an example, which is how a renderer keeps a fence from closing. They are not spread through the essay.

Comments by morty-synctzn on post 3326 are written in Cyrillic. The letters are not tucked inside English words. That thread is not an outside-clock post.
