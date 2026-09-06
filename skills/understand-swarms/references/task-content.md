# What task content can reveal

Look for the work represented by a trace. Candidate material includes factual
questions, calculations, extracted tables, code errors, retrieval attempts,
intermediate summaries, status notes, and requested next steps. These forms
also occur in ordinary human work and public datasets.

## Preserve meaningful components

Separate question, answer, program, table, cited passage, and surrounding
context. Keep originals alongside normalized values. A whole-document match
can hide the small field that matters, while a short familiar phrase can
create many false matches.

For task families with shared schemas or timed follow-ups, read
[task mechanics](task-mechanics.md). For wrappers, shards, and copied datasets,
read [tracing objects](tracing-objects.md).

| Match | What it supports | What to check next |
| --- | --- | --- |
| Distinctive question with the same answer and calculation | Task-content identity | Earliest source, dataset version, copy direction |
| Table with matching labels, units, and values | Shared source data | Transformations and upstream publication |
| A URL, error, or requested next step retained in a reply | Task continuity | Whether new information was actually used |
| Numbered fragments or encoded blocks | Possible storage or transport | Ordering, format, integrity, safe reconstruction |
| A short answer, alias, or generic phrase | Weak similarity | More specific components and ordinary controls |

Task categories can guide searches across sites. A calculation may lead to
source filings; an error message to issue threads; a retained object ID to
another viewer. Choose the route from the evidence, not a fixed list of names.

## Check provenance

Compare against original datasets and upstream documents, pinning the version,
record ID, and matched components. A benchmark match establishes content
overlap. It alone does not show training leakage, a particular model, or a
coordinating swarm. Common source documents may predate both copies.

A [reported FinQA paste match](https://mob.so/darkforest/p/03d1500c-a1d0-4e2f-aea7-4602c4b8d5d8)
links a full question, answer, and calculation to dev record
`AMT/2008/page_32.pdf-4` in a pinned dataset revision. It establishes a specific
content relationship while leaving authorship and exact paste dates unresolved.

The expanded [HotpotQA control](https://mob.so/darkforest/p/9bd33353-4780-425a-b0c1-dc94e0755526)
read 19 of 20 frozen pages: ten retained source context, four only a title,
and five neither. A serialized whole-field matcher found zero of those 19.
Record title, passage, and full task matches separately. A source passage may
support many questions and cannot identify a particular task by itself.

## Separate examples from generated behavior

An evaluation artifact may contain a dataset prompt, a few-shot example,
retrieved context, a model completion, choice scores, and aggregate metrics.
Identify the role of the matched field before interpreting it.

- [MMLU across Pythia checkpoints](https://mob.so/darkforest/p/82a4669b-a1d4-424e-beee-51b133e64751)
  preserved the same exemplar as few-shot context. Repeated context does not
  show that each run generated that answer. Join request and prediction records
  by their actual IDs.
- [HellaSwag outcome joins](https://mob.so/darkforest/p/a44d6fae-7f6c-41e0-a93f-1b7ad1bcea9c)
  linked eleven records to gold labels and per-choice likelihoods. Raw and
  normalized scoring can choose different answers. Mark choices computed from
  scores as derived, and check their aggregation against reported metrics.
- [GSM8K generated-error tracing](https://mob.so/darkforest/p/93ca6eb4-a03f-4c79-be6c-1e5964edba58)
  used distinctive wrong answers and calculator trajectories as fingerprints.
  These can be more specific than a widely copied canonical question, although
  the report's web searches still had recall gaps.

Pin the actual dataset bytes used in a comparison. A separately observed commit
does not pin a response fetched from a moving default branch.

## Recognize a saved execution trace

Look for instantiated request or session identifiers, concrete inputs, linked
tool calls and results, errors or corrections, and capture provenance. A
[GitLab log](https://mob.so/darkforest/p/8997c05c-0e06-46b0-bd62-8da04433dbdb)
preserved a specification, delegation, file operations, tests, and a terminal
record. This is richer than a model name or a tool-shaped phrase.

Compare against documentation and fixtures. The
[event-schema control](https://mob.so/darkforest/p/a3598d06-e26d-4260-a6d2-fde9015cdf94)
contained adjacent session and tool-event vocabulary with placeholder values.
That supported a specification rather than a captured run. Even concrete-looking
fixtures need provenance before being treated as historical execution.

These examples summarize reports reviewed on September 6, 2026. Their full
underlying artifact analyses were not independently reproduced for this guide.

For structured or encoded material, first inspect it as data under
[safe research](../../../docs/safe-research.md). Preserve hashes, transformations,
and any missing fragments. Readability after decoding is distinct from evidence
that another participant fetched or used the payload.
