# Collection and resumption

## Design the source adapter

Inspect the surface before choosing a traversal. Keep discovery references and
complete fetched records distinguishable, even if one endpoint returns both.

| Surface | Useful discovery route | Limitation to verify |
| --- | --- | --- |
| Wiki or forum | Recent changes, feed, topic index, revision API | Whether bodies, edits, and older revisions are accessible |
| Registry or repository | Public owner namespace, release list, tree, commits | Whether search covers metadata, files, historical versions, or only recent items |
| Paste or shared object | Observed public IDs, public index, explicit source links | Whether any enumerable index exists and how long objects remain available |
| Dataset or archive | Pinned export, shard manifest, capture index | Whether the sampled files and dates represent the claimed population |

Record the endpoint or query, ordering, cursor behavior, stable object ID,
timestamp meaning, body location, and supported history. Keep request scope
within the scan specification. Follow public read routes under
[safe research](../../../docs/safe-research.md), including redirect checks.

A useful adapter exposes discovery, record retrieval, and typed extraction
with explicit failures. Use the project's interface conventions. Preserve raw
responses where practical so a parser fix can be tested without another fetch.

## Choose the traversal mode

**Historical backfill:** Freeze a date window, upper bound, revision, or manifest
when the source supports it. Persist each page's continuation token. If live
insertions can shift numbered pages, overlap requests and deduplicate by stable
IDs. Report the resulting snapshot limitations. Stop at a documented end or the
requested boundary; a repeated cursor without progress is a stalled traversal.

**Monitoring:** Start from a saved watermark with enough overlap to cover the
source's observed lag. Deduplicate the overlap and revisit tracked records when
edits or comments do not appear in the creation feed. Keep a backfill checkpoint
separate from the current monitoring position. A latest-items feed may have an
irrecoverable gap after a long pause; report it and use history if available.

**Reanalysis:** Read saved bodies with new parser or matcher versions. Retain
their original retrieval and source times. Save the new analysis alongside its
version and evidence references. Re-fetch only where the question requires a
current state or the stored evidence is insufficient.

## Preserve progress through failures

Persist records and continuation state atomically where the storage supports
it. Otherwise save evidence first and make replay idempotent. Advance a
collection cursor only when all discovered references on that page are stored,
with either retrieved evidence or a durable retry record for unresolved work.
Unresolved fetches remain visible in coverage.

A fetched body that fails extraction can remain in storage while collection
continues. Record the parser error and leave processing incomplete. A repair
must retry that body before it can count as successfully analyzed. Keep the
processing version and completion status separate from fetch status.

Use conditional requests when supported and a prior body is retained. Preserve
earlier evidence if a page later disappears. Record an unavailable response;
establish deletion only when the provider supplies that evidence.

Respect retry delays for throttling, back off transient failures, and stop
retrying within the run when its allocation is spent. Authentication or access
denials need an explicit status rather than a no-match result. Unexpected HTML,
a challenge page, or a changed response schema should fail extraction visibly.
Bound download size, expansion, concurrency, and elapsed time for the workload.

Use a single-run guard or the existing scheduler's concurrency control for
shared state. Save the current continuation point when stopping. A restarted
run should recover unfinished work without erasing prior coverage.

## Report the run

Keep counts for discovered references, fetched bodies, successful extractions,
matched records, distinct candidates, and reviewed findings. Include actual
source date ranges, pages completed, unresolved failures, remaining cursors,
and why the run ended. A completed traversal, a budget-limited sample, and a
failed fetch support different conclusions. Measure requests, elapsed time,
and any model usage against the user's allocation.
