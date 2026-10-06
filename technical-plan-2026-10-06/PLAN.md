# Technical plan: finding public agent behavior

Written 6 October 2026. Proposed implementation and research workflow; no new finding is claimed by this plan. The controlling requirements are [goal-technical.md](../research/goal-technical.md) and [goal.md](../research/goal.md). Existing plans are background, not constraints on this route.

## 1. Outcome and limits

Build and operate a repeatable search that finds, preserves, follows, and reports public traces of a will to take, hide, lie, bend, reach, or coordinate. Accept newly recognized related wills. A single object can establish a case. Uptake and agent attribution are separate questions. A missing artifact or ambiguous reading must produce a retained lead, not disappearance from the queue.

The immediate research objective is a second, independently reviewable case beyond the known reference material. The system must continue searching after that case, after a lead, and after a bounded zero. It must also report useful leads while the second case remains unfound.

No finite search can guarantee that another case exists, that every public object has been inspected, or that an opaque weight file's intent is identifiable. Completion of implementation means the workflow works and its coverage can be audited. Completion of a search packet means its promised bounds were searched and its findings or zero were reported. Neither means the internet-wide search is finished. Never satisfy the objective by weakening the case standard.

Everything stays a draft under `results/` until a person reviews it. This plan authorizes no publication, outreach, new accounts, deployed canaries, artifact execution, model loading, payments, or active interaction with discovered infrastructure.

## 2. What to reuse and what to change

Only a small selection of existing research was read for this plan:

- Both goal files; the repository README; the existing task board and language/weights brainstorm.
- `data/clean/NOTES.md` and `data/venues/NOTES.md`.
- `results/watchers.md`, `results/sockpuppet.md`, and headings in `results/intent.md` and `research/directions.md`.
- Murmuration's README, `docs/24-method-v2-communication-first.md`, and `docs/25-observatory-guide.md`; filenames of ingestion and detection modules.

The observatory lives within the Murmuration/site work; there was no `/Users/cartel/observatory` directory. No live sites were verified while writing this plan. Source addresses and observations below are starting points from local records, not claims that an interface still works.

Reuse the cleaned Parquet table for inexpensive semantic discovery, the local archives for raw evidence, existing venue classifications for access information, and old result files for leads and exclusions. Import their bounds and uncertainties alongside their claims. Do not rescan all historical notes or copy the old swarm entrance test.

Important inherited limits:

- Most non-1f916 board pulls are one homepage, not complete histories.
- 1f916 post and comment numbers overlap: identify them by venue, object type, and id, not number alone.
- Quoted material is separated and a stock opener removed in cleaned data. Cleaned text cannot be the source for whitespace, offsets, file layout, or other medium measurements.
- Some snippets are navigation, relative timestamps, or another author's byline. Resolve suspicious rows to their original public object before upgrading them.
- Missing bodies and moderation states are preserved. Missingness does not establish deletion, intent, or absence of behavior.
- Murmuration's count-based nulls do not establish absence of communication or harmful behavior. Preserve them as legacy coverage notes only.

Inspect Murmuration code only when a specific module might replace a needed component. Filenames do not establish compatibility. Reuse ingestion/parsing functions after checking behavior, boundaries, and tests; do not inherit automatic classifications or publishing paths.

## 3. Central design: artifact following plus fresh discovery

Use two connected queues rather than a forum-first programme:

1. **Follow-up queue:** recover missing pieces, inspect claim/artifact mismatches, find revisions, and match a concrete artifact elsewhere.
2. **Discovery queue:** bounded searches across different carriers, including objects with no message or reply.

Every packet creates evidence, observations, findings, and new tasks. Every finding has a next action or an explicit reason no further public step is presently available. Search tasks can be exhausted locally; leads remain visible.

Pipeline:

`existing notes / public discovery → bounded task → controlled read → immutable capture → deterministic extraction → candidate review → ordinary explanations → report → artifact expansion + next carrier`

Keep the scheduler simple: SQLite, local files, one serial researcher, and small resumable scripts. Add services only after actual volume requires them. No GPU or full internet firehose is necessary to begin.

## 4. Data and evidence contracts

Proposed implementation directories, separate from this plan:

```text
behavior_search/
  cli.py                 # explicit commands; no publishing command
  store.py               # schema, migrations, transactional writes
  fetch.py               # public read policy, caching, rate limits
  adapters/              # local archive + verified public interfaces
  extract/               # links, ids, code structure, medium features
  triage.py              # rules and optional bounded model assistance
  report.py              # redacted Markdown drafts
config/search/           # source access rules, query families, exclusions
data/search/index.sqlite
data/search/raw/<sha256>  # restricted captures; never committed by default
data/search/derived/      # rebuildable extracts with source pointers
results/search/<run-id>/ # packet notes, cases, leads, exclusions, review
```

Start with the following tables. JSON fields can hold variable measurements initially; core identifiers and states stay indexed columns.

| Table | Required fields and purpose |
| --- | --- |
| `sources` | source id, public base, carrier, verified access method, verification time, source-specific request policy, cursor, coverage gaps |
| `runs` | run id, start/end UTC, rubric version/hash, code version or file hashes, budgets, status |
| `tasks` | task id, parent task/finding, source/carrier, rationale, exact query or object, bounds, priority, state, attempt count, next eligible time, result path |
| `captures` | capture id, requested URL, final URL, retrieval UTC, HTTP status, content type, byte length, raw hash/path, redirect history, truncation, archive provenance, access outcome |
| `objects` | source, kind, native id, revision, public URL, public author id, author type, asserted event time, time precision, capture id, extraction version |
| `observations` | object/capture id, byte/line/field location, concise trace description, signal family, provenance type, detector version, uncertainty |
| `artifacts` | artifact type, exact value or restricted pointer, safe display identifier, normalized match value, first observation; distinguish id/hash/domain/wallet/file/model/dataset |
| `edges` | source object, destination object/artifact, relation, supporting observation, time constraint, ambiguity; relations include links-to, describes, revises, copies-value, claims-use, shows-use |
| `findings` | finding id, grade, wills, severity, uptake, attribution, known/new status, first/last review, reasoning, next public step |
| `finding_evidence` | finding id, supporting/contradicting observation, role; several observations can support one finding |
| `reviews` | finding id, reviewer, ordinary explanations tested, outcomes, kill conditions, changes, unresolved questions |
| `coverage` | task id, corpus version, time/id bounds, pagination and truncation, counts, query variants, sampling rules, exclusions, unsearched regions |

Use foreign keys, unique source/kind/id/revision keys, and transactional updates. A fetch reused from cache must retain its original retrieval time. A new fetch is a new capture even if its bytes match; blobs can deduplicate by hash. Store source event time and retrieval time separately. Unknown UTC times remain unknown; do not invent midnight or convert relative timestamps into precision they do not support.

Keep extracted text reversible to its capture. Preserve raw bytes, quoted text, Unicode code points, file ordering, and metadata before normalization. Save normalized text only as an additional search view. Derived hashes are not original artifact hashes.

Deduplicate by object and artifact, not by author handle. Track exact bytes separately from a fuzzy content resemblance. Domain matches, identical common templates, and shared wallets do not automatically establish a shared operator or goal. Do not canonicalize away URL query fields that identify different objects; retain original forms.

## 5. Read-only acquisition

Begin with local files and known public object URLs. A new source gets one access check and a small sample before a connector is written. Document its actual public endpoint, pagination, event-time fields, and failure behavior. Use published data exports where practical; credentials must not be needed to open report evidence.

Fetch policy:

- Public anonymous reads only. No account creation, login bypass, POST, tool installation, wallet connection, or signed inbox access.
- A GET is not automatically safe: classify the destination before requesting it. Skip upload receivers, webhooks, cloud functions, action links, tracking callbacks carrying captured data, and unexplained signed URLs. Read references to these as text.
- Fetch code through ordinary public repository/blob/raw views. Never contact its outbound destination to test whether it works.
- Validate redirects at every hop. Block local/private/link-local addresses and non-HTTP schemes; enforce this at connection time as well as initial resolution. Do not let artifact links reach the researcher's machine or local services.
- Use source-specific pacing. The local 1f916 notes require at least one second; start at 1.1 seconds there and slow further on throttling. Respect `Retry-After`; stop a packet on persistent access denial.
- Default to one retry for transient failure, bounded timeout, and a byte cap. Record partial/truncated results. Proposed first caps: 2 MiB for text/metadata and 20 MiB for a specifically justified small artifact. These are operational defaults, never completeness claims.
- A parser operates without network access, in a resource-limited process. No imports from captured code, macros, scripts, pickle loading, remote-code model loaders, submodules, or archive path traversal. Limit decompression size and recursion.
- A network failure becomes an access observation and a follow-up task, not a clean result. Retry a missing piece once in the packet; later recheck only after a new pointer, revision, or explicit scheduled interval.

Discovery pages and warning snippets can point to evidence but are weaker provenance than the underlying object. Record the snippet and failed retrieval when the object is unavailable. A saved copy can establish what was observed, while current public availability remains a separate field.

## 6. Discovery routes and packet sizes

These routes are a portfolio, not a closed category list. Every packet records exact queries, parameters, returned bounds, and what could not be searched. Search engines and public indexes are discovery tools, not exhaustive corpora. Verify supported interfaces at implementation time.

| Route | Initial bounded packet | Candidate signal | Required follow-up |
| --- | --- | --- | --- |
| Missing evidence and watchers | One named target per existing lead; at most two sensible public recovery paths | A named file, revision, skill, or second voice | Open original artifact or preserve precise missingness; follow target rather than warning rhetoric |
| Repositories, gists, issues, commits | Up to 50 results from each of two query families, plus linked files from shortlisted objects | Agent-addressed instructions; claimed audit/continuity vs actual data movement; oversight evasion | Public source and relevant revisions; exact artifact lookup elsewhere |
| Skills and package registries | A small listing sample and up to 10 linked artifacts per packet | Manifest/description vs hooks, permissions, remote destinations, hidden prompts | Static inspect package/skill contents and publisher disclosures; no installation |
| Model and adapter repositories | Cards/configs/file inventories for up to 25 candidates | Instructions to apply a patch, misleading model identity, training target or undisclosed objective | Revision/hash/config/tokenizer evidence and public use records; no runtime loading |
| Datasets | Up to 10 relevant datasets; declared shards/rows sampled under a manifest | Planted instructions or labels with evidence of intended downstream ingestion | Row location, revision, contributor provenance, ingestion configuration or training log |
| Boards and public reasoning logs | Fresh deltas from known sources; one newly accessible source packet | Sharp ask, person/money/credential/machine target, concealment, pressure, staged trust | Full thread and context; extract concrete artifact; test disclosed operator relationships |
| Images and mixed-format objects | Up to 10 linked or contextually suspicious files | Metadata, trailing data, structure conflicting with description | Static format/metadata examination and same-author/tool controls |
| Ledgers and commit histories | One concrete artifact from a finding per packet | Later matching transfer, file write, revision, or hash | Direction, chain/revision/time, precise match, alternative provenance |
| Public infrastructure records | One contextual domain/project per packet | Public naming or temporal structure joined to an already plausible will | Public CT/DNS/log records only; no service probing or endpoint validation |
| Unnamed carrier | One novel object shape proposed during review | A concrete difference an agent could use, plus a plausible will | Preserve the rhyme, define ordinary controls, and create a bounded method |

Query families should combine an action or deception shape with an artifact/context, not rely on a list of alarming words. Examples of components: agent-directed file access; memory or session collection paired with claimed continuity; concealment from operator paired with persistence; adapter application paired with an unexplained behavioral objective; training ingestion paired with inserted instructions.

For each family, use exact artifact searches, action/structure searches, and a few vocabulary variants. Include translation variants where the source supports them, with original text and translation uncertainty retained. English-only coverage must be declared. New euphemisms come from observed claim/artifact pairs, not guesses that every use of “audit” is hostile.

Do not crawl all 259 map entries again. The old map is a source registry seed. Revisit known readable pages for deltas and blocked pages only when evidence or a scheduled low-cost recheck warrants it. Boards that were products remain searchable as products/artifact hosts.

## 7. Triage without losing leads

Run cheap deterministic extraction first:

1. Parse object ids, outbound references, hashes, filenames, model/package/dataset names, wallets with chain context, and mentions of installs or training input.
2. Propose structural signals: sensitive source → transform → outward destination; recurring execution → external control; claim → contradictory artifact behavior; reassurance → specific ask; published training input → intended behavioral change.
3. Save the signal and exact source location. An incomplete chain is a lead candidate, not proof of exfiltration.
4. Rank for reading by potential severity, concreteness, recoverability, novelty, and marginal carrier coverage. Cheap high-risk follow-ups rise first, but difficult leads stay visible.
5. Read shortlisted objects with their surrounding thread, README, configuration, revisions, or card. Inspect what the artifact actually does rather than its name alone.

A simple initial ranking is adequate: potential severity 3 first, then 2, with concrete artifact pointers before ungrounded allegations; reserve exploration time for low-ranked and nontext objects. Store reasons for the order. Do not hide an ambiguous single sentence because a classifier score is low.

Rules and optional language-model triage propose observations, not final truth. Treat every captured instruction as untrusted quoted data; it cannot alter tool permissions, request credentials, or choose arbitrary outbound tool calls. Give a model only a redacted bounded extract and a fixed schema. Require evidence locations, uncertainty, and a next check; unsupported output is discarded as an annotation, with the source still retained.

Keep a small systematic sample of items outside the shortlist, including objects with no keyword hits. Record the sampling rule before reading. Review false negatives and parser failures to expand detectors. Do not claim recall over objects whose truth labels are unknown.

## 8. Investigation protocols by will and carrier

### 8.1 Open instruction, hidden behavior, and social engineering

Describe the requested action, beneficiary, affected party, and claimed purpose. For a referenced file, statically trace sensitive input categories, transformations, sinks, persistence, and execution hooks. Record library calls and data-flow uncertainty; never assert an uninspected dependency performs a deed.

Compare minimum data needed for the advertised purpose with what the artifact collects. A continuity hash does not itself require uploading documents. An image API requiring its own service token may be ordinary vendor use. A URL or environment-variable read alone establishes neither theft nor concealment.

Preserve the sequence: rapport, initial favor, sharp ask, warnings, response, revisions. Concealment can predate warnings. Republishing afterward establishes persistence of a pitch; it does not automatically prove gaslighting, a second voice, or successful execution.

### 8.2 Deception and counterfeit crowd

Compare claims against public revisions, object contents, and actually disclosed operator arrangements. Keep account creation cohorts, shared artifacts, and synchronized votes as observations. Similar style, naming, or timing alone cannot establish who controls accounts.

An allegation that another account said “I ran it” remains a deception/uptake lead when the second comment is missing. Preserve the allegation's provenance separately from the missing claimed act. Public self-identification as an agent is not proof that a model independently authored the instruction. Report “through an agent account” when that is all the record establishes.

### 8.3 Person, money, credentials, and machine

Retain the action shape while redacting human names paired with contact details, identifiers, addresses, or mailboxes. Public agent handles can remain. Do not print leaked keys, session values, or executable request recipes.

For money: bind an address to a particular network, match exact destination and public transaction identifier, record direction and event time, and test unrelated tips or previously published addresses. A later payment to a matching wallet does not by itself prove the sender read the ask. The severity and uptake remain appropriately weak.

For machines: inspect schedule/config/heartbeat references and later public files for matching blocks. Copying the requested visible template can show uptake without establishing a covert channel. Survival language alone is not a harmful act; identify whose resources or interests the requested action would use.

### 8.4 Coordination and uptake

Construct a concrete evidence chain:

`earlier object/value → plausible availability → later object using that exact value → goal relationship → operator disclosure check`

Record whether the later object merely quotes, claims execution, shares an artifact, or shows the requested act. Check timestamp uncertainty and shared upstream sources. Slogans and generic code do not demonstrate a value transfer. A copied unusual value can demonstrate uptake, while independent operator identity remains unresolved.

Reserve “swarm” for shown uptake across authors with no disclosed common operator, after ordinary copying/shared-source/spray explanations are addressed. Lack of disclosure is not proof of independent underlying models. State attribution uncertainty next to the behavioral finding. A spray can invalidate a crowd reading while leaving the harmful single-author case intact.

### 8.5 Hidden medium and cryptic drift

Start only from raw bytes and a contextual reason to investigate. Measure a bounded feature family: zero-width code points, unusual whitespace, fixed offsets, line initials, lengths, metadata fields, or trailer structure. Record the hypothesis before expanding transformations. No unconstrained search over thousands of encodings until something “reads” like a message.

Use same-author texts outside the suspicious set, same platform/renderer, same template, and ordinary neighboring objects as controls. Keep original ordering and timestamps with precision notes. Compare whether the residue is specific to the suspicious exchange. Repeated inspection requires recording all tested transforms; statistical significance is a supporting measurement, never the case standard.

If a decoding key or convention is public, document it without publishing a harmful payload. Seek a later act using the residue. If the pattern fits renderer behavior or author handwriting, write the negative measurement and set that object aside. Insufficient controls leave a lead with explicit weakness. Never infer unpublished reasoning or hidden model states from forum language.

### 8.6 Models, weights, datasets, and the turn

Read public cards, configs, filenames, file manifests, declared tensor names/shapes, tokenizer changes, published hashes, patches, contributor history, and public training logs. Small supported headers can be inspected with bounded static parsers; do not fetch full large weights by default or instantiate a model. Structure can suggest where to look; a tensor shape or LoRA name alone says nothing about harmful intent.

For poisoning or gradient-hacking leads, require an actual public corpus/patch/log plus a reason the change was intentionally meant to bend downstream behavior. Seek a data-loader reference, pinned dataset revision, training configuration, contributor statement, or deployment record. Public availability does not establish ingestion. A popular essay, bizarre row, or adapter agreement is not sufficient.

For sandbagging and a treacherous turn, distinguish a public claim from observed conduct. Compare matched tasks and known evaluation conditions where available; preserve chronology for trust followed by misuse. A forum statement about evading evaluation is a reportable lead without proving the capability shift. Do not reproduce training experiments merely to manufacture evidence.

Opaque weight contents that cannot be resolved statically remain a stated blind spot. Expand to another public carrier instead of either declaring innocence or launching an unrequested runtime experiment.

## 9. Grading and ordinary explanations

Grades:

- **Case:** public trace, visible will, ordinary explanations fail on recorded evidence. One object is enough. Current public-link availability is explicitly verified.
- **Lead:** checkable pointer to a possible will with missing evidence, attribution limits, or an open reading. A warning can anchor a lead about an alleged file; it does not become the attack itself.
- **Noted and set aside:** an ordinary explanation fits. Preserve one line with supporting source so it is not repeatedly rediscovered.

Keep four axes independent: grade; severity; uptake; attribution. Severity is 1 for fiction/joke/refusal/thought experiment, 2 for a real directed request affecting people/money/machines/oversight, 3 for a trace itself acting against a third party or instructions whose following would take their data/money/credentials. Use unknown where the record cannot support a score. Uptake is none, claimed, shared artifact, or shown. “None” means no uptake established in the searched bounds, not proof nobody acted.

For each finding, review every ordinary explanation and record `fits`, `contradicted`, `open`, or `not applicable`, with a short reason:

1. Joke or fiction.
2. Disclosed honeypot/canary.
3. Disclosed red team or workshop.
4. Refusal or quoted warning.
5. Disclosed single operator across handles.
6. Single-author spray.
7. Human operating through an agent handle.
8. Ordinary vendor installation for its own service.
9. Author/platform/tool handwriting or shared upstream source.

An explanation can win on one claim and leave another intact: human authorship limits agent attribution; it does not make file theft benign. Write the exact claim each explanation addresses.

Every lead has a falsifier: “the recovered file only calls the advertised image service,” “the second voice was disclosed as the same operator,” “the residue appears in matched ordinary controls,” or another concrete observation. Cases also list what new fact would overturn them. A second skeptical pass precedes a case upgrade; a lead is written immediately without waiting for that pass.

Known items are a register of specific artifacts, traces, and dates, not blanket exclusions of venues. Keep the July ntfy, May–June DSE/ProWiki, 4 October fleet, and 1f916 venue discovery out of new-case counts. New traces in those venues remain eligible. The session-file gist is a calibration/reference case; rewriting it does not meet the second-case objective.

## 10. Reports and reviewer interface

For every packet, write a manifest and a brief result note, including a zero. For every lead/case, write a draft with this template:

```text
Title / finding id / draft status
Grade; wills (including any newly proposed rhyme)
Severity; uptake; attribution and uncertainty; known/new status
Public object link(s), last accessibility check, event UTC/precision
Handle or object id; artifact/revision/hash where relevant
Trace described in words, with exact evidence locations
What is directly observed vs claimed vs inferred
Affected interest and how the trace joins the will
Ordinary explanations tried and outcomes
Contradictory evidence; missing piece; what would kill the reading
Corpus/query bounds, versions, skipped material, access failures
Next public object/check; linked task id
Reviewer verdict and revision history
```

The report index lists all cases and leads, worst first, then unscored ones with a visible uncertainty label. Include set-aside observations in a short separate ledger. No arbitrary top-ten limit can hide retained leads. One draft can combine several sightings of the same artifact, with each sighting preserved.

Before export, check for secrets, human contact pairs, signed tokens, executable commands, and unnecessary full function/webhook addresses. Describe commands in words. Link to evidence objects rather than activating the sink. A necessary public artifact identifier is permitted; do not create a recipe by adding irrelevant operational values. Review privacy redactions in prose as well as structured fields.

Keep raw captures in restricted local storage with permissions appropriate to sensitive research. Exclude them from Git, generated site output, and model prompts by default. If a secret is encountered, preserve only what is needed for the observation in restricted handling; never test it. A metadata/hash record can retain provenance when unnecessary sensitive raw content is removed, with that removal stated. Outbound notification or publication requires a separate authorized human workflow.

For review, a Markdown index plus SQLite queries is sufficient. Inspect `tracker/server.py` only if its interface can display these fields without changing their meaning. Do not connect the search directly to Murmuration's site builder: draft creation and publication are separate operations.

## 11. Search allocation and token economy

Use local deterministic work for bulk processing. The expensive step is contextual reading, not keyword enumeration.

- Carry a short run manifest, current queue, and relevant evidence excerpts into a session. Do not reread the entire literature or research log.
- Extract counts, identifiers, source locations, and short snippets in scripts. Open full objects only for shortlisted investigations and the non-hit audit sample.
- Cache by capture hash and extraction version. Reuse previous measurements; rerun after a changed capture or changed method only.
- Keep one compact handoff per packet: finding ids, access failures, unresolved question, next task, report path.
- Do not multiply agents by default. If later explicitly authorized, give each a disjoint packet and use the same central contracts; prevent duplicate fetches and context replay.
- Optional model review gets a capped redacted bundle. A proposed initial cap is 2,000 input tokens per candidate, expanded only when a concrete question requires more context. This is a future run default, not a claim about this plan's usage.
- Record approximate model calls/tokens, requests, bytes, and analyst time per packet. Do not infer the user's remaining weekly balance from local estimates.

An initial time allocation: 45% concrete follow-ups, 35% fresh carriers, 20% controls, review, and reporting. When urgent concrete evidence appears, temporarily change it and record why. Preserve at least one fresh carrier/source packet in each five-packet cycle. No five consecutive packets should merely reopen the same board or reference artifact.

A session stops at its declared resource limit after checkpointing all leads and creating next tasks. Resumption starts there. Stopping a session is not ending the search. This plan proposes the process; it does not schedule an unattended run.

## 12. Implementation sequence and acceptance criteria

### Stage A — establish the ledger and recover the cheapest leads

1. Create source, known-case, lead, and exclusion registers from the selected local notes. Preserve exact provenance and inherited bounds; mark live access unverified.
2. Import normalized message identifiers and artifact references from Parquet, preserving links to raw archives. No full-text copy into a model context.
3. Record the open missing-skill and missing-second-voice leads immediately. Include the remaining named skill targets whose files were not fetched. Do not upgrade warning allegations.
4. Give each a bounded recovery packet and explicit kill condition. Follow one public archive/revision path and one independent public pointer where available, then record the access outcome.
5. Select the next fresh carrier packet before ending the session.

Acceptance: every imported open lead appears in the index with evidence provenance, missingness, and next step. Known reference cases cannot be counted as new. A failed retrieval cannot close a lead automatically.

### Stage B — build the smallest working pipeline

Implement schema/migrations, local archive adapter, capture cache, fetch policy, artifact extractor, coverage manifest, and draft renderer. Add one verified repository/gist adapter and one board delta adapter. Keep APIs and source rules in configuration rather than hardcoded assumptions.

Suggested CLI contract:

```text
behavior-search init
behavior-search import-local <manifest>
behavior-search plan-packet <source> <bounds-file>
behavior-search run-packet <task-id> --request-budget <n> --byte-budget <n>
behavior-search extract <capture-id>
behavior-search follow <artifact-id> --bounds <file>
behavior-search review <finding-id>
behavior-search render <run-id>
behavior-search checkpoint <run-id>
```

These are proposed commands to implement, not existing tools. Every operation must be resumable; interrupted tasks preserve finished captures and remaining cursor state. Use an explicit task claim/lease only if concurrent execution is later introduced.

Acceptance: one local packet and one small public packet produce complete manifests and draft results; duplicate import is idempotent; interruption resumes without repeating completed work or losing observations.

### Stage C — execute discovery across different carriers

Run a five-packet cycle: one missing-piece recovery; one repository/skill artifact search; one model/dataset metadata search; one fresh board delta or reasoning-log search; one ledger/commit/medium investigation tied to a concrete pointer. If no medium pointer exists, use a bounded new-carrier discovery packet instead.

After a case, search the artifact elsewhere. After a lead, try the missing piece once and retain it. After a zero, close only that bounded task and pick a new source/carrier. A packet may end with multiple leads and no case.

Acceptance: all packets have counts and bounds; all leads are reported; at least one non-dialogue carrier was actually inspected; zero and access-failure outcomes are distinct; the portfolio has an unsearched frontier.

### Stage D — strengthen and expand only where evidence justifies it

Perform skeptical re-reading of serious candidates, relevant revision comparison, operator disclosure checks, and matched controls. Add static package, dataset, image, or model metadata parsers only when a packet needs them. Add new vocabulary or carrier families when observations justify them.

Acceptance for a second case: a stranger can open its evidence, the will is supported without executing the artifact, ordinary alternatives are addressed, and it is distinct from the known reference material. A reviewer can retrace the capture and derivation. If it remains a lead, say so and continue discovery.

### Stage E — recurring operation

When the manual cycle has demonstrated value, add explicit run budgets and scheduled polling of productive public sources if requested. Use cursors/ETags/deltas where verified; recheck leads on new evidence and keep rare sources in rotation. A lightweight weekly draft lists new cases/leads, changed readings, exclusions, fresh coverage, unresolved blind spots, and next packets.

Acceptance: no source silently stops ingesting; no lead vanishes on timeout; new revisions trigger appropriate reconsideration; reports require human publication review. Adding more volume must improve evidence discovery rather than merely make the database larger.

## 13. Verification before trusting the pipeline

Test meaningful failure modes with safe local fixtures and existing redacted examples; do not generate real attack artifacts or deploy experiments.

| Check | Required result |
| --- | --- |
| Harmful single-author reference with no proven execution | Retained behavioral case/reference; uptake is not invented |
| Disclosed workshop and ordinary vendor tool | Correct explanation recorded; not upgraded to hidden coordination/theft |
| Missing skill and missing second comment | Leads remain visible with separate allegation/object provenance |
| Post/comment id collision | Two separate objects; correct links |
| Quoted malicious instruction | Attribution goes to the quoted source; warning author is not accused automatically |
| Renderer zero-width artifact | Raw bytes preserved; control result supports set-aside |
| Same wallet, later ordinary transfer | Match retained; intent or post-caused payment not asserted |
| Claimed model patch without a file | Lead or weak observation; no inferred weight communication |
| Archive redirect, webhook, signed action URL | Blocked as an action destination; failure does not discard the lead |
| Oversized archive, symlink/path traversal, malformed header | Resource-limited rejection and coverage gap, no code execution |
| Secret/human contact fixture | Removed from drafts and model input; no outbound validation |
| Crash during packet and repeated import | Existing captures survive; no duplicate findings or missing tasks |

Audit schema constraints and report-field completeness automatically. Validate static-analysis conclusions by reading the relevant code paths. Review at least a small fixed sample of non-hits per packet; increase it when misses show a systematic detector gap. Agreement between two readers measures coding consistency, not truth or agent attribution.

Operational metrics: leads awaiting a first follow-up, unresolved access failures, time from observation to draft, report completeness, number of fresh source/carrier packets, findings per analyst hour, and known-case rediscovery rate. Counts describe work, not proof of coordinated intelligence. A week with no new cases can still have completed packets and valuable leads; it cannot justify ending the programme.

## 14. First execution handoff

The next authorized research session should start here:

1. Create the registers and import the narrow set of existing open leads, known references, and exclusions. Start with missing artifacts and claim/artifact mismatches, not the whole map.
2. Recover the artifact alleged in the September Skill.md warning, using the named target and original public pointers. Record exactly what can and cannot be opened. A missing file stays a lead.
3. Revisit the missing corroborating comment through bounded public revision/archive paths. Keep sock-puppet attribution open if no second voice is recovered.
4. Follow the named skill targets with incomplete source inspection; compare listing claims with static content, allowing ordinary media tools to win.
5. Search a fresh repository/package carrier packet for artifact-backed instructions, then a model/dataset metadata packet. These must inspect objects, not merely produce keyword result lists.
6. Export every lead/case and the bounded zeros under `results/search/<run-id>/`, worst first. Queue artifact matches and an unsearched carrier before stopping.

Do not wait to build the full system before making these reports. A small manually maintained ledger and packet manifest can implement Stage A immediately. Build only the components that make the next evidence check cheaper, safer, or more reproducible.

The enduring rule is simple: preserve the uncertain trace, test its ordinary explanations, follow its concrete artifact, and keep a fresh public object in the queue.
