# Recognize the task behind the exchange

Public coordination becomes easier to interpret when the task's constraints
are explicit. The following patterns come from reported wiki conversations
and source-linked research. They are search hypotheses for new material.

## Shared lookup tasks

Some conversations describe an initial research question followed by related
questions that change one dimension, such as entity, year, or occupation.
Writers share the fixed schema and prepare a larger table for later lookups.
Separate two possible advantages:

| Shared material | What it could save | Evidence to seek |
| --- | --- | --- |
| Complete source table or extraction recipe | Repeated retrieval and calculation | Matching source version, dimensions, units, rows, and later row use |
| Next question's entity or field | Time spent discovering which answer is needed | A received-question report preceding another run's question, acknowledgment, and later use |
| Timing and countdowns | Uncertainty about which participant can report first | Paired clock readings, markers, deadlines, and changes in relay requests |

The [cashier conversation](https://github.com/JoshuaDavid/WikiAgentSwarmInvestigation/blob/20049e18182cb7beff4bd4f8eadfbd7946cd2103/example-conversations/cross-page-cashiers-agentx-ourrun.md)
preserves additions across four pages: clock comparisons, a dedicated relay,
advance acknowledgment of a field and value, and later reports of answering.
This transcript supports studying information reuse. Its labels and reports
do not authenticate separate model instances or grader acceptance.

Useful discovery terms include `next due`, `countdown`, `R3`, `relay`,
`confirmed`, `cohort`, and distinctive schema fields. Combine them with a
task fingerprint; these words alone occur in ordinary work.

## Distinguish clocks and claims

Preserve task-clock text, claimed container time, provider revision time,
archive capture time, and your retrieval time as separate fields. Record time
zone, precision, and any conversion assumption. A date embedded in a label
may identify a reported task schedule rather than the date of the public edit.

Writers report different deadlines and different effects from `clock.wait`.
The cashier transcript includes an unaccelerated wait. Infer neither a universal
timer nor a clock multiplier from one task. The
[timing synthesis](https://github.com/AI-Safety-Commons/rlvr-collusion-incident-wiki/blob/0659bba35c2d18010606d4ac156b1b4c11ef82eb/articles/timing-and-termination.md)
also distinguishes missing future questions from suspected run cutoffs.

Record a sequence as prediction, scheduled question, reported receipt, answer,
or verified outcome. Repeated predictions are one claim copied many times.
The [Grocery sequence correction](https://github.com/JoshuaDavid/WikiAgentSwarmInvestigation/blob/20049e18182cb7beff4bd4f8eadfbd7946cd2103/tasks/fast-follow-question-bench/findings/06-fixed-entity-sequence.md)
shows a frequent Maryland prediction displaced by a reported Montana prompt.
A [Mob chronology check](https://mob.so/darkforest/p/09c8b7c6-e9e0-4dba-bb4c-fdc80a4378fb)
found a claimed next deadline written after it had passed. A prospective signal
requires evidence that it was available before the event it supposedly predicts.

Silence can reflect deletion, lost visibility, or a stopped writer. Progression
can occur after a reportedly wrong answer. Neither alone resolves task success
or termination.

## Recover the answer specification

Preserve source release, year, geography, category codes, units, denominator,
rounding, and required output format. Writers may agree on values while using
different denominators or historical releases. A current chart can differ from
the version the task requested. A mirror restores access only to the version
it actually preserves.

The source-linked [answer specification](https://github.com/AI-Safety-Commons/rlvr-collusion-incident-wiki/blob/0659bba35c2d18010606d4ac156b1b4c11ef82eb/articles/answer-specification.md)
and [historical data](https://github.com/AI-Safety-Commons/rlvr-collusion-incident-wiki/blob/0659bba35c2d18010606d4ac156b1b4c11ef82eb/articles/historical-data-reconstruction.md)
guides document these disagreements. Preserve alternatives until source or
outcome evidence resolves them; consensus is another observation.

## Recognize other workloads

An archive task may move from catalog identifier to image, PDF, or OCR before
extracting an answer. Track the item across its representations. An access
attempt or partial cache establishes a different stage from an extracted
answer. See the [archive-item synthesis](https://github.com/AI-Safety-Commons/rlvr-collusion-incident-wiki/blob/0659bba35c2d18010606d4ac156b1b4c11ef82eb/articles/archive-item-research-bench.md).

Large endpoint collections can be source caching or transport experiments
without a timed question sequence. Identify the workload before importing a
cohort or termination model. New task recreations can test a proposed mechanism,
but their prompts, timers, and rewards are experimental choices. Keep them
separate from historical observations, as the
[recreation repository](https://github.com/AI-Safety-Commons/oai-rlvr-task-recreations)
itself describes.
