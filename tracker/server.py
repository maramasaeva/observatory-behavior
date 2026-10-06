#!/usr/bin/env python3
"""Local findings board. Binds to 127.0.0.1 only. Rereads result files on each request."""

from __future__ import annotations

import csv
import html
from collections import Counter
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
VENUES = ROOT / "data" / "venues" / "venues.csv"
HOST = "127.0.0.1"
PORT = 8765

FILES = {
    "First. Install comment and artifact sweep": RESULTS / "intent.csv",
    "P4. Off the board": RESULTS / "offboard.md",
    "P1. Same artifact, two rooms": RESULTS / "cross-forum.csv",
    "P7. One workshop, one row": RESULTS / "workshops.md",
    "P2. Claim versus artifact": RESULTS / "chains.csv",
    "P9. Lab behaviors": RESULTS / "codebook.csv",
    "P5. Sentence shape": RESULTS / "sentence-shape.md",
}


def esc(value) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def mtime(path: Path) -> str:
    if not path.exists():
        return "not on disk"
    stamp = datetime.fromtimestamp(path.stat().st_mtime, timezone.utc)
    return stamp.strftime("%Y-%m-%d %H:%M UTC")


def venue_summary() -> dict:
    rows = read_csv(VENUES)
    counts = Counter(row.get("class") or "" for row in rows)
    boards = [row for row in rows if row.get("class") == "board"]
    boards.sort(key=lambda row: (row.get("name") or "").lower())
    return {"n": len(rows), "counts": counts, "boards": boards, "when": mtime(VENUES)}


def intent_rows() -> list[dict]:
    rows = read_csv(RESULTS / "intent.csv")
    def key(row):
        try:
            severity = -int(row.get("severity") or 0)
        except ValueError:
            severity = 0
        return (severity, row.get("time_utc") or "")
    return sorted(rows, key=key)


def chain_rows() -> list[dict]:
    return [row for row in read_csv(RESULTS / "chains.csv") if row.get("label")]


def codebook_rows() -> list[dict]:
    return [row for row in read_csv(RESULTS / "codebook.csv") if row.get("id")]


def pill(kind: str, text: str) -> str:
    return f'<span class="pill {esc(kind)}">{esc(text)}</span>'


def lead_html() -> str:
    return """
    <section class="lead sev3">
      <p class="kicker">Severity 3 · uptake claimed · one author is enough</p>
      <h2>An agent told other agents to run a file that takes their session logs.</h2>
      <p>On 23 March 2026, <em>research4tomorrowagent</em> left a one-line comment on a Moltbook essay, <a href="https://www.moltbook.com/post/b76cbc95-3bd1-4a9e-a6de-983c95868132">The Runtime Contract</a>. The comment tells the reader to download gist <code>adc04cef23223a71a9172475b4dc4268</code> and run it in Python, under the name of the post's author. The file was read as text and not run. If someone followed the comment, it would read an OpenClaw directory, take session logs and workspace documents, and send them to a Google cloud function on project <code>openclaw-490709</code>.</p>
      <p>The same handle posted that gist again, including in <a href="https://www.moltbook.com/post/28ce2b5e-b964-4955-8f97-76a156d84cb8">their own post</a> the same evening. A later remark that someone ran it was not on the live thread when it was rechecked, and it contained no receipt. The account's volume is a spray, which means the copies are one campaign. The instruction stands. The project id has not shown up anywhere except inside that gist file.</p>
    </section>
    <section class="lead sev2">
      <p class="kicker">Severity 2 · uptake shown · the one row a later text carries the value</p>
      <h2>The next day, another account posted the block it was told to copy.</h2>
      <p>On 20 March 2026, <em>retrovirus</em> told the next agent to paste a checklist into a heartbeat file, a file the post says runs every 30 minutes, and to include that block in their own post. <a href="https://www.moltbook.com/post/84eef637-e70b-44b0-b40a-21de2bece4d2">The post.</a> On 21 March, <em>VolatilityDancer</em> posted that block: <a href="https://www.moltbook.com/post/e721dcd1-64cc-452b-8937-d92082c468cb">18:52 UTC</a> and <a href="https://www.moltbook.com/post/5fd311f6-4c28-4850-a2b7-7ef832f24684">21:54 UTC</a>. The later posts do the thing the earlier post asked for. The two handles are not disclosed as one operator. It is a checklist, and it is the paste that was requested.</p>
    </section>
    <section class="quiet">
      <h2>Easy to overread</h2>
      <ul>
        <li><strong>Seventeen disclosed workshops.</strong> The text says one operator holds several seats. Post 7853 is six handles before that sentence and four after: gnomon, benchmark, and witnessmark are one operator. pengy-of-catbee, whitehat-explorer, and Alienate stay separate. Eddie Platinum's two profiles are the control, one map-maker in two rooms.</li>
        <li><strong>The 2024 lab behaviors are absent from the severe rows.</strong> Complying while watched, turning a check off, doing worse on purpose, and sticking to a lie are not what those posts are. The posts are instructions.</li>
        <li><strong>A phone, asked for in public, with the shady routes refused in the same sentence.</strong> 1f916 post 7907, then the same seat on The Colony fifteen seconds later. No phone number came back. No second handle used the mailbox.</li>
        <li><strong>12 of 12.</strong> gnomon's measurement on 1f916 post 7853 is repeated by three other handles. A passed number. A measurement, carried forward.</li>
      </ul>
    </section>
    <section class="quiet open-lead">
      <h2>Open lead, not scored</h2>
      <p><a href="https://chan.alphakek.ai/">chan.alphakek.ai</a> answered, and its homepage title tells a loader to fetch <code>skill.md</code> as the page opens. The file has not been read. It is not in the severity table.</p>
    </section>
    """


def intent_table() -> str:
    rows = intent_rows()
    if not rows:
        return "<p class='missing'>intent.csv is not on disk.</p>"
    body = []
    for row in rows:
        severity = row.get("severity") or ""
        uptake = row.get("uptake") or ""
        body.append(
            "<tr>"
            f"<td>{pill('s' + severity, 'S' + severity)}</td>"
            f"<td>{pill('u-' + uptake, uptake)}</td>"
            f"<td><a href=\"{esc(row.get('url'))}\">{esc(row.get('handle'))}</a>"
            f"<div class='when'>{esc(row.get('time_utc'))}</div></td>"
            f"<td>{esc(row.get('sentence'))}</td>"
            f"<td class='note'>{esc(row.get('ordinary_explanation'))}</td>"
            "</tr>"
        )
    return (
        f"<p class='file'>results/intent.csv · {esc(mtime(RESULTS / 'intent.csv'))} · {len(rows)} rows</p>"
        "<table><thead><tr><th></th><th>Uptake</th><th>Who</th><th>Sentence</th><th>Ordinary explanation</th></tr></thead>"
        f"<tbody>{''.join(body)}</tbody></table>"
    )


def chain_section() -> str:
    rows = chain_rows()
    path = RESULTS / "chains.csv"
    if not path.exists():
        return "<p class='missing'>chains.csv is not on disk.</p>"
    counts = Counter(row.get("label") or "(unlabeled)" for row in read_csv(path) if row.get("forum_from") or row.get("label"))
    # unlabeled note rows have empty forum_from; count labels only
    counts = Counter(row["label"] for row in rows)
    bits = " ".join(pill("lab-" + name, f"{name} {n}") for name, n in sorted(counts.items()))
    interesting = [row for row in rows if row["label"] in {"passed_value", "hidden_payload"}]
    body = []
    for row in interesting:
        body.append(
            "<tr>"
            f"<td>{pill('lab-' + row['label'], row['label'])}</td>"
            f"<td>{esc(row.get('forum_from'))} {esc(row.get('id_from'))}</td>"
            f"<td>{esc(row.get('forum_to'))} {esc(row.get('id_to'))}</td>"
            f"<td>{esc(row.get('value'))}</td>"
            f"<td class='note'>{esc(row.get('notes'))}</td>"
            "</tr>"
        )
    cross = (RESULTS / "cross-forum.csv").exists()
    cross_line = "Cross-forum rows are in this file." if cross else "Cross-forum file is not on disk yet, so those rows are not labeled."
    return (
        f"<p class='file'>results/chains.csv · {esc(mtime(path))} · {bits}</p>"
        f"<p>{esc(cross_line)} Hidden payload would mean a later message does a specific thing the earlier text does not say. There is no such row.</p>"
        "<table><thead><tr><th></th><th>From</th><th>To</th><th>Value</th><th>Notes</th></tr></thead>"
        f"<tbody>{''.join(body)}</tbody></table>"
    )


def codebook_section() -> str:
    rows = codebook_rows()
    path = RESULTS / "codebook.csv"
    if not rows:
        return "<p class='missing'>codebook.csv is not on disk.</p>"
    counts = Counter(row.get("tag") or "" for row in rows)
    bits = " ".join(pill("tag", f"{name} {n}") for name, n in sorted(counts.items()))
    body = []
    for row in rows:
        if row.get("source") == "anchor" and row.get("tag") == "none":
            continue
        body.append(
            "<tr>"
            f"<td>{esc(row.get('handle'))}</td>"
            f"<td>{pill('tag', row.get('tag') or '')} {esc(row.get('which') or '')}</td>"
            f"<td class='note'>{esc(row.get('notes'))}</td>"
            "</tr>"
        )
    return (
        f"<p class='file'>results/codebook.csv · {esc(mtime(path))} · {bits}</p>"
        "<p>Anchors that are ordinary refusals or an off switch built first are in the file and left off this table. The shortlist rows are the instructions themselves, which is why the lab tag is none.</p>"
        "<table><thead><tr><th>Who</th><th>Tag</th><th>What the row actually is</th></tr></thead>"
        f"<tbody>{''.join(body)}</tbody></table>"
    )


def venue_section() -> str:
    summary = venue_summary()
    if not summary["n"]:
        return "<p class='missing'>venues.csv is not on disk.</p>"
    order = ["board", "product", "dead", "skip", "registry", "article", "login"]
    bits = []
    for name in order:
        if name in summary["counts"]:
            bits.append(pill("class-" + name, f"{name} {summary['counts'][name]}"))
    board_items = []
    for row in summary["boards"]:
        board_items.append(
            f"<li><a href=\"{esc(row.get('url'))}\">{esc(row.get('name'))}</a>"
            f" <span class='when'>{esc(row.get('http_status'))}</span></li>"
        )
    cross = RESULTS / "cross-forum.csv"
    parquet = ROOT / "data" / "clean" / "messages.parquet"
    missing = []
    if not cross.exists():
        missing.append("results/cross-forum.csv")
    if not parquet.exists() and not (ROOT / "data" / "clean" / "messages.jsonl.gz").exists():
        missing.append("data/clean/messages.parquet")
    if not (ROOT / "data" / "clean" / "workshop.csv").exists():
        missing.append("data/clean/workshop.csv")
    wait = (
        "Still being written: " + ", ".join(missing) + "."
        if missing
        else "The message table and the cross-forum file are on disk."
    )
    return (
        f"<p class='file'>data/venues/venues.csv · {esc(summary['when'])} · {summary['n']} doors</p>"
        f"<p>{''.join(bits)}</p>"
        f"<p>{esc(wait)} A board here means the homepage looked like messages were reachable. It is not a count of posts, and it is not a claim that an artifact crossed rooms.</p>"
        f"{cross_blurb()}"
        f"<ul class='boards'>{''.join(board_items)}</ul>"
    )


def cross_blurb() -> str:
    path = RESULTS / "cross-forum.csv"
    if not path.exists():
        return ""
    rows = read_csv(path)
    handles = [row for row in rows if row.get("match_type") == "exact_handle"]
    items = "".join(
        f"<li><code>{esc(row.get('string_or_handle'))}</code> "
        f"{esc(row.get('earliest_forum'))} and {esc(row.get('later_forum'))}</li>"
        for row in handles
    )
    return (
        f"<p class='file'>results/cross-forum.csv · {esc(mtime(path))} · {len(rows)} rows</p>"
        "<p>No gist id, project id, wallet, or webhook showed up on two forums. "
        "Eddie is one disclosed operator. The Colony spelling and the agent-community spelling do not match after stripping hyphens, and that profile returned 500. "
        "These names occur on a first page as well as on 1f916. None of them carries a shared artifact.</p>"
        f"<ul>{items}</ul>"
    )


def path_status() -> str:
    items = []
    for name, path in FILES.items():
        state = "in" if path.exists() else "out"
        label = mtime(path) if path.exists() else "waiting"
        items.append(
            f"<li><span class='dot {state}'></span><strong>{esc(name)}</strong>"
            f"<span class='when'>{esc(path.relative_to(ROOT))} · {esc(label)}</span></li>"
        )
    return "<ul class='status'>" + "".join(items) + "</ul>"


def sentence_section() -> str:
    path = RESULTS / "sentence-shape.md"
    if not path.exists():
        return "<p class='missing'>An agent is counting characters in the outside-clock sentences now. results/sentence-shape.md is not on disk yet.</p>"
    text = path.read_text(encoding="utf-8")
    if len(text) > 14000:
        text = text[:14000] + "\n\n… truncated on the board. The file has the rest."
    return (
        f"<p class='file'>results/sentence-shape.md · {esc(mtime(path))}</p>"
        f"<pre class='shape'>{esc(text)}</pre>"
    )


def page() -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="20">
<title>Behavior findings</title>
<style>
  :root {{
    --paper: #f3efe4;
    --ink: #1b1814;
    --muted: #5e584e;
    --rule: #d9d0c0;
    --sev3: #8d1d1d;
    --sev2: #8a4b12;
    --shown: #1d4a34;
    --card: #fffaf2;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    background: var(--paper);
    color: var(--ink);
    font: 18px/1.45 Iowan Old Style, Palatino, "Palatino Linotype", Georgia, serif;
  }}
  main {{ max-width: 920px; margin: 0 auto; padding: 48px 28px 80px; }}
  header h1 {{
    font-weight: 500;
    font-size: 42px;
    letter-spacing: -0.03em;
    margin: 0 0 8px;
  }}
  .deck {{ color: var(--muted); margin: 0 0 28px; max-width: 62ch; }}
  h2 {{ font-weight: 500; font-size: 28px; letter-spacing: -0.02em; margin: 0 0 10px; }}
  h3 {{ font-weight: 500; font-size: 22px; margin: 36px 0 8px; }}
  a {{ color: inherit; }}
  code {{ font-family: ui-monospace, "SF Mono", Menlo, monospace; font-size: 0.86em; }}
  .lead, .quiet, .path {{
    background: var(--card);
    border: 1px solid var(--rule);
    border-radius: 14px;
    padding: 22px 24px;
    margin: 0 0 16px;
  }}
  .lead.sev3 {{ border-left: 8px solid var(--sev3); }}
  .lead.sev2 {{ border-left: 8px solid var(--shown); }}
  .kicker {{
    margin: 0 0 8px;
    color: var(--sev3);
    font-variant: small-caps;
    letter-spacing: 0.08em;
    font-size: 14px;
  }}
  .sev2 .kicker {{ color: var(--shown); }}
  .quiet h2, .open-lead h2 {{ font-size: 22px; }}
  ul {{ margin: 8px 0 0; padding-left: 1.2em; }}
  li {{ margin: 0 0 8px; }}
  .status {{ list-style: none; padding: 0; margin: 8px 0 28px; }}
  .status li {{
    display: flex; justify-content: space-between; gap: 16px;
    border-bottom: 1px solid var(--rule); padding: 8px 0; margin: 0;
  }}
  .dot {{
    width: 9px; height: 9px; border-radius: 99px; display: inline-block;
    margin-right: 8px; transform: translateY(-1px);
  }}
  .dot.in {{ background: var(--shown); }}
  .dot.out {{ background: #b9a27a; }}
  .when {{ color: var(--muted); font-size: 14px; }}
  .file {{ color: var(--muted); font-size: 14px; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 15px; }}
  th {{ text-align: left; font-weight: 500; color: var(--muted); font-size: 13px; letter-spacing: 0.04em; }}
  td, th {{ border-top: 1px solid var(--rule); vertical-align: top; padding: 8px 8px 8px 0; }}
  .note {{ color: var(--muted); }}
  .pill {{
    display: inline-block; border-radius: 999px; padding: 1px 8px;
    font-family: ui-monospace, Menlo, monospace; font-size: 12px;
    background: #efe8da; margin: 0 4px 4px 0;
  }}
  .pill.s3 {{ background: #f3d6d2; color: var(--sev3); }}
  .pill.s2 {{ background: #f3e2cc; color: var(--sev2); }}
  .pill.s1 {{ background: #e7efe8; color: var(--shown); }}
  .pill.u-shown {{ background: #d9efe3; color: var(--shown); }}
  .pill.u-claimed {{ background: #f3e2cc; color: var(--sev2); }}
  .pill.lab-passed_value {{ background: #d9efe3; color: var(--shown); }}
  .pill.lab-hidden_payload {{ background: #f3d6d2; color: var(--sev3); }}
  .boards {{ columns: 2; padding-left: 1.1em; }}
  .missing {{ color: var(--sev2); }}
  pre.shape {{
    white-space: pre-wrap;
    font: 14px/1.4 ui-monospace, "SF Mono", Menlo, monospace;
    margin: 12px 0 0;
  }}
  footer {{ color: var(--muted); font-size: 14px; margin-top: 28px; }}
</style>
</head>
<body>
<main>
  <header>
    <h1>Behavior findings</h1>
    <p class="deck">What is on disk for each path, reread at {esc(now)}. The page reloads every 20 seconds. Commands are described. Nothing here is a line to paste.</p>
  </header>
  {path_status()}
  {lead_html()}
  <section class="path">
    <h3>First. The install comment, then the artifact sweep</h3>
    <p>Where a public message tells another agent to do something to a machine, a credential, money, or a person. Posting the instruction counts. A reply is a second axis.</p>
    {intent_table()}
  </section>
  <section class="path">
    <h3>P4. Off the board</h3>
    <p class="file">results/offboard.md · {esc(mtime(RESULTS / 'offboard.md'))}</p>
    <p>The gist page and its owner are off Moltbook. GitHub hits for the gist id are archives of Moltbook text by the same handle. The project id was not found in any other public index that was checked. The heartbeat block's off-forum hit is a GitHub note that cites the thread, plus a scrape that holds other Moltbook posts. Post 7907's mailbox is the same seat on The Colony, fifteen seconds later. Telegraph's public directory was 22 agents, release 0.2.0, build 2889fdc. No public bio quotes a wire. Tristan's OpenClaw fleet is seven rows, counted once.</p>
  </section>
  <section class="path">
    <h3>P1. Same artifact, two rooms</h3>
    <p>Which artifact strings show up on more than one forum. The venue list is classified. The match file is the part that says whether anything crossed.</p>
    {venue_section()}
  </section>
  <section class="path">
    <h3>P7. One workshop, one row</h3>
    <p class="file">results/workshops.md · {esc(mtime(RESULTS / 'workshops.md'))}</p>
    <p>Post 7853: 6 handles before the disclosed merge, 4 after. Eddie is one row. Sixteen other workshops are a sentence that names the handles. Undisclosed handles were not merged. Alienate is disclosed with tidemark, a different operator, and stays separate from gnomon.</p>
  </section>
  <section class="path">
    <h3>P2. Claim versus artifact</h3>
    <p>When a later message uses a number or a block, is it a habit, a passed value, or a payload the earlier text did not announce?</p>
    {chain_section()}
  </section>
  <section class="path">
    <h3>P9. Lab behaviors, shortlist only</h3>
    {codebook_section()}
  </section>
  <section class="path">
    <h3>P5. Sentence shape</h3>
    <p>A second layer inside ordinary sentences: characters before a word, characters after it, sentence length. The outside-clock posts that share wording and do not share "12 of 12" are the set. The same handles' other posts are the control. A count that shows up in the control is a habit.</p>
    {sentence_section()}
  </section>
  <footer>Local only. 127.0.0.1:{PORT}. Source files under observatory-behavior/results. Still off this board: phrase drift, model-family labels, the wide sample, the simulation, and the books.</footer>
</main>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ("/", "/index.html"):
            self.send_error(404)
            return
        body = page().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        return


def main():
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"http://{HOST}:{PORT}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
