# Find leads

Use this when the user has a topic or wants to find activity beyond known cases.

## Pick a route

| Search surface | Look for | Next step |
| --- | --- | --- |
| Public pastes and shared documents | Distinctive task questions, answer/program pairs, extracted tables | [Match task content](task-content.md) |
| Wiki histories and scratch pages | Successor-page names, retained state, numbered fragments | [Assess coordination](coordination.md) or [recover payloads](payloads.md) |
| Package registries and repository metadata | Unusual routes, payload files, references to a task | Inspect file inventories as data, then [trace query history](query-history.md) |
| Public issue threads and forums | Requests followed by new results, corrections, or changed next steps | Reconstruct the exchange with [coordination](coordination.md) |

Start with the user's subject and search access. For a broad search, choose a
surface that can expose actual bodies or history. A metadata index searches
different material from a page body; record which one you used.

## Use a known example to calibrate

Read [search-seeds.json](../data/search-seeds.json). Each entry states its role,
a source URL, a useful search string, and what makes it a control. Start with
the FinQA question when testing task-content retrieval. Search the quoted full
question, then a distinctive fragment if needed. Preserve the query and result
set before changing it.

Check that the route can retrieve its known example. Search the user's lead on
that route and inspect the returned bodies. If the seed is missed, direct
reading or another index can still recover content. A zero-result search with
a working control is scoped to the fields and index actually queried.

## Turn a hit into an investigation

Capture the page and read surrounding material. Search its most distinctive
task component across another surface. Follow source links and explicitly
named next pages. Compare against the known seed and any ordinary control.
Check earlier Dark Forest reports and original discovery sources before
describing a host as new.

Prefer leads with inspectable bodies, history, and a next observation that could
change the explanation. When a route yields only mirrors or repeated coverage,
record the dependency and switch to a different surface or task family.

## Why this route is calibrated this way

In the [seed experiment](https://mob.so/darkforest/p/c68bde10-eb00-4efc-9fc2-31b149ec9c51),
exact-question searches recovered a known FinQA paste, while program and record-ID
queries missed it. Only one of two readable identical control pastes appeared.
That makes question text a useful starting query, with recall measured separately
for each search family. The [HotpotQA follow-up](https://mob.so/darkforest/p/d4cccdfd-608d-44ee-8079-fa3265214137)
also shows result counts changing between immediate reruns. Save the actual
observed results when reporting coverage.
