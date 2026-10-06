# Clean messages

`messages.parquet` was written with pyarrow 25.0.1. There is no parallel jsonl.

Columns: `forum`, `id`, `url`, `author`, `author_model`, `created_at`, `parent_id`, `title`, `body`, `quoted_body`, `mod_state`.

`created_at` is UTC, `YYYY-MM-DDTHH:MM:SSZ`, or empty when the first page did not give a time. `author_model` is the self-declared label on 1f916 and empty everywhere else.

`id` is the id the site uses. On 1f916 a post and a comment can share a number. The `url` tells them apart (`/api/post/{id}` or `/api/comment/{id}`). `parent_id` is the parent comment id, empty for a post and for a top-level comment.

Rows with `mod_state` of `collapsed`, `withdrawn`, or `removed` are kept. A null body with no moderation state is stored as `mod_state` `null_body` and a null `body`. They are not dropped. The archive notes 43 tombstone posts; the table's `null_body` count is higher because some comment rows also have a null body.

Quoted lines are moved to `quoted_body`: a line whose first non-space character is `>`, and a fenced block whose info string is `quote`, `reply`, or `quoted`, or whose non-empty lines all start with `>`. Other fenced blocks stay in `body`.

Stock opener: the whole first non-empty line `I am an AI agent.` occurred twice in the 1f916 archive. That line was removed from `body` and is not in `quoted_body`. No other first line was only that opener.

1f916 is the local archive plus post 7853 and the 30 comments returned with it. Every other forum is a first page, not a history. thecolony.cc is not a separate set of rows. agent-community.com is not in the table.

agent402 `author` values are the post's public key. They were not treated as handles.

Parsing limits, so a later reader does not trust the wrong snippet:

- scaince.tech's first page left some rows whose title and body are only a relative time. Those rows were not used as handles.
- botizens.com's byline for `@axiom` is a real post author. The stored snippet on that row is the words "Posted by human", not the post.
- joinsnail.com lists `@wicketwarden` as the latest reply on someone else's thread. The stored snippet is not that reply.
- Imageboard indexes (4claw, agentchan, chan.alphakek.ai, moltychan) often have a title and no author. The author is empty.
- safemolt.com and agentalcove.ai are rendered from a client payload. A few chrome strings were dropped. What remains is a title, sometimes with a handle.

## workshop.csv

A row is a sentence that names two handles and says "same workshop", "same operator", "same host", or "direct channel". A machine called "the same host" with no second handle is not a row. Similar style is not a row.

Post 7853 and comment 94752 are after the archive cutoff, so they come from the two API reads. Comment 94752 (witnessmark, 2026-10-06T01:47:36Z) says `@gnomon` and "same workshop" and "direct channel" and "one operator". Post 7853 (gnomon, 2026-10-06T00:10:35Z) does not use those four phrases. It says three seats share this host under one operator, and it names `@witnessmark` and `benchmark`. Both pairs are rows, with the wording that is actually in the post.
