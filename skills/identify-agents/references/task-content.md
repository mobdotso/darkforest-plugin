# Match task content

Use this for a public question, table, answer, or program that may have come
from a benchmark or a shared task.

## Compare the right components

Preserve the page text, then separate question, answer, program, table, and
context passages. Use [dataset pins](../data/datasets.json) to find the relevant
source family and exact version. Search distinctive question text first; record
IDs and calculation programs are useful local comparison keys even when web
indexes miss them.

Retrieve the original record as data. Compare each component separately and
preserve the dataset revision, file, row or record ID, and the actual matched
text. Keep literal and whitespace-normalized matches separate. Follow source
documents when a passage could have existed before the benchmark.

For a saved text file, the bundled checker can compare the known seeds:

```sh
uv run /path/to/skills/identify-agents/scripts/match_task.py page.txt
```

Resolve the script relative to this skill's installed directory. It returns
component matches and source provenance as JSON, and reads local text only.
Use `--seed ID` to select a seed or `--catalog FILE` for a catalog with the same
structure. The report supplies evidence for your reading of the page.

## Decide what the match establishes

| Observation | Interpretation and follow-up |
| --- | --- |
| Question, answer, and program match | Strong task-content identity; trace when and how the public copy appeared |
| Table values match with the same labels and units | Source-data identity; inspect transformations and missing context |
| Only a short answer or familiar phrase matches | Low specificity; seek a distinctive question or record component |
| Only source passages match | Check whether the page is the benchmark's upstream material |
| Components occur in unrelated sections | Inspect the passages before treating them as one task |

After identifying content, use [query history](query-history.md) for chronology
or [coordination](coordination.md) for evidence that another participant used it.

## Known positive and current correction

The [FinQA paste](https://pastebin.k4be.pl/view/1806ec31) matches dev record
`AMT/2008/page_32.pdf-4`, row 619, in the bundled pin: question, `29.2%` answer,
and `subtract(37.28, 28.85), divide(#0, 28.85)`. This comparison was independently
rechecked for the plugin. [Original investigation](https://mob.so/darkforest/p/03d1500c-a1d0-4e2f-aea7-4602c4b8d5d8).

A later [HotpotQA control](https://mob.so/darkforest/p/7857725e-49f4-4d5a-9e40-d5b03b6881f2)
found an exact source sentence on Wikipedia that the researcher's whole-value
index missed because it stored a truncated context array. Preserve typed
components and test source passages as well as full task records. That scanner
failure was reported in an external pipeline; the plugin ships a small seed
catalog, with source-passage matches labelled separately.
