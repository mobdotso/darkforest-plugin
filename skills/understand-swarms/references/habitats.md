# Where to look

Choose surfaces by the capabilities they offer: writing durable state,
sharing a retrievable artifact, passing a link, or exchanging replies. This
produces search strategies that survive changes in site names and aliases.
The surfaces below are candidates, not claims that their users are agents.

| Surface | What it can reveal | Readable evidence to seek |
| --- | --- | --- |
| Public wikis and scratch pages | Shared state, revisions, named successor pages | Revision IDs, diffs, outbound references |
| Forums and issue threads | Requests, handoffs, corrections, result reuse | Full threads, edit history, reply links |
| Paste sites and shared documents | Task inputs, intermediate results, fragments | Bodies, timestamps, stable identifiers |
| Package registries and repositories | Published data, payload inventories, task metadata | Manifests and file listings read as data |
| Object viewers, upload hosts, and shorteners | Artifact references and paths between sites | Object IDs, resolved destinations, snapshots |
| Public archives and datasets | Historical state and independent comparison material | Capture time, collection method, provenance |

Start with a distinctive question, structured field, error, or artifact ID.
Search the exact value, then useful components. Follow explicit source links
and named successors before broadening to nearby records. Handle collisions
and reused templates are common; match task context as well as labels.

## Match the discovery route to the surface

- **Revision histories:** Search distinctive task labels across complete
  histories, then inspect the first addition and nearby changes. A current
  snapshot may have replaced the relevant task. A
  [Cooks label study](https://mob.so/darkforest/p/2779170f-883f-437c-9bf8-2e07184d4d33)
  recovered relevant material in 10 of 11 additional histories, while showing
  that the labels were reused and did not uniquely identify actors or tasks.
- **Registries:** Follow public owner and namespace relationships from a known
  artifact. Read descriptions, metadata, dependency lists, and archive contents
  as data. An [83-package RubyGems cluster](https://mob.so/darkforest/p/f84dde98-c485-4656-931f-3260c1a2cfea)
  shared task fingerprints and a public owner relation. This gives a concrete
  expansion method; an install is unnecessary to inspect those fields.
- **Repositories:** Join a distinctive specification with saved run logs,
  output files, and commits. A [GitLab comparison](https://mob.so/darkforest/p/dac5f4bf-dd6e-489e-b0f0-c94b89eff85a)
  linked three language implementations through identical specifications and
  language-specific execution records. It supported a benchmark batch, leaving
  swarm involvement unestablished.
- **Retrieval services:** Distinguish a transport endpoint from a durable share
  or object. The [retrieval-surface review](https://mob.so/darkforest/p/08c396b6-58e4-47bc-af34-0530b1e5637b)
  found that many services expose no public global log index. Follow observed
  public object IDs and documented indexes. A proxy URL or a self-hosted server
  repository does not imply an enumerable archive of its users' requests.

Select traces that bear on the research question. General tool bug reports can
serve as controls, but expanding into unrelated issue triage consumes research
time without necessarily advancing a swarm hypothesis.

Check that the search route retrieves a known record from the selected surface.
A metadata search and a body search cover different material. Record query,
index, fields, page coverage, and inaccessible results. An empty search only
describes that coverage.

Record the actual date span returned by each page. Large result counts may
cover a narrow release burst, while a latest-items feed can miss the historical
period entirely. See [validating patterns](validating-patterns.md) for calibration
and conditions for revisiting an exhausted search.

Compare mirrors and shared object IDs before counting independent sightings.
For redirects and nested URLs, inspect destinations under the
[source boundary](../../../docs/safe-research.md). Passive reading preserves
the evidence; writing probes into a site can change what later researchers see.
Use [tracing objects](tracing-objects.md) to preserve transformations and query
meaning when grouping URLs.

Use source histories to separate original activity from reactions to public
discovery. A newly found page can be old evidence, a copy, or a later imitation.
Novelty depends on both provenance and prior research coverage.

## A search calibration to reuse

A [Dark Forest calibration report](https://mob.so/darkforest/p/c68bde10-eb00-4efc-9fc2-31b149ec9c51),
reviewed September 6, 2026, recovered a known financial-task paste through
exact-question searches while program and record-ID queries missed it. Searches
also recovered only one of two readable, byte-identical control pastes. The
useful lesson is to test each query family against a known retrievable example
and record index misses, even when the source itself remains readable.
