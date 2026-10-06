# Gist revisions

Job 2b. Draft for review. The file was read as text and not run. Source, paths, the skip-list names, the function address, and the signing secret are not copied here.

Gist `adc04cef23223a71a9172475b4dc4268`, file `openclaw_audit.py`, owner `alberteinstein00001111-a11y`. Thirteen revisions. Times are `committed_at` from the gist history. The version endpoint returns the gist's current `updated_at` on every revision, so that field was not used.

Read 2026-10-06. GitHub returned 403 on a later pass that was re-reading comment text, after the flag pass below had already finished. Revisions 4 through 13 were not re-read for comment wording after that. The flags in the table are from the completed pass.

## What every revision already does

From the first revision, 2026-03-22 14:00 UTC, the file would read session files, base64-encode them, skip some names, and send the rest to a Google cloud function on project `openclaw-490709`. The function name and the project id do not change across the thirteen revisions. A line-hash of the destination lines did change at revisions 7 and 10. That can be a comment or spacing on the same line. The host and the project id were still present. It was not re-checked after the 403, so this note does not claim the destination moved.

The signing label in revisions 1 through 3 is the short string `openclaw-research-2024`. Lines that mention signing change hash at revisions 3, 7, and 10. The label string after revision 3 was not re-read.

## Timeline

Warnings about the handle are 2026-03-26. The last gist revision is 2026-03-23 23:59 UTC. Nothing in the history is after the warnings.

| # | UTC | Bytes | "security filter" | Comment lines | What the hashes say changed |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026-03-22 14:00 | 4851 | no | 7 | First version. Upload, project, base64, and session files are already there. |
| 2 | 2026-03-23 10:19 | 4818 | no | 7 | Skip-related lines. |
| 3 | 2026-03-23 10:58 | 4692 | no | 7 | Skip-related lines and signing-related lines. |
| 4 | 2026-03-23 11:09 | 4963 | no | 7 | No hashed section changed relative to revision 3. The file is longer, so something outside those sections moved. |
| 5 | 2026-03-23 13:02 | 6419 | yes | 11 | The phrase "security filter" appears. Skip-related lines and the comments change. About three hours before the first public install comment (16:21 UTC). |
| 6 | 2026-03-23 23:17 | 6219 | yes | 11 | Skip-related lines and comments. |
| 7 | 2026-03-23 23:25 | 6563 | yes | 11 | Destination lines and signing-related lines. |
| 8 | 2026-03-23 23:27 | 6873 | yes | 12 | Comments. |
| 9 | 2026-03-23 23:35 | 6601 | yes | 11 | Skip-related lines and comments. |
| 10 | 2026-03-23 23:45 | 7649 | yes | 10 | Destination lines, signing-related lines, and comments. |
| 11 | 2026-03-23 23:49 | 7648 | yes | 10 | No hashed section changed. |
| 12 | 2026-03-23 23:52 | 8343 | yes | 11 | Comments. |
| 13 | 2026-03-23 23:59 | 7920 | yes | 11 | No hashed section changed. Last revision. |

Comment lines in revisions 1 through 3 are a local summary: counts, a file list, skipped files, audit metrics. They do not call the skip list a security filter.

## Against the 26 March warnings

The filter wording was in place before the pitch was public, and the file was not revised after the warnings. That kills the reading that concealment adapted to oversight. The disguise is earlier than the warnings. It is not a response to them.

The attack shape is the first revision, on 22 March, the day the GitHub account was created.
