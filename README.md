# Dark Forest

A plugin for Codex and Claude Code that helps agents investigate public websites
used as task memory or shared workspaces. It packages methods, search seeds,
dataset pins, and comparison cases from the [Dark Forest mob](https://mob.so/darkforest).

## Use it

Give your agent a page to investigate or a subject to search:

| Request | Where the agent starts |
| --- | --- |
| Find public traces of agents working on a shared task | Search routes and calibrated seeds |
| Investigate this paste and identify where its task came from | Component matching and pinned dataset records |
| Work out whether these pages passed information between them | Query histories and source/successor comparisons |
| What changed in Dark Forest's methods? | Live feed index, original reports, and corrections |

The [investigation skill](skills/identify-agents/SKILL.md) selects the relevant
guide as the evidence develops. The [feed skill](skills/read-darkforest/SKILL.md)
reads current research. Results explain the observed activity, the evidence
for agent involvement, and what would resolve the remaining uncertainty.

## Load in Claude Code

From a local checkout, start Claude Code with:

```sh
claude --plugin-dir /path/to/darkforest-plugin
```

Then ask naturally or invoke a skill directly:

```text
/darkforest-plugin:identify-agents Investigate this page: <URL>
/darkforest-plugin:read-darkforest What investigation methods changed recently?
```

The Claude manifest follows the
[Claude Code plugin format](https://code.claude.com/docs/en/plugins-reference).
The Codex manifest is retained for Codex installation. Both load the same skills
and supporting files; all runtime references stay inside the package.

## What the agent can use

| Resource | Purpose |
| --- | --- |
| [Find leads](skills/identify-agents/references/find-leads.md) | Choose a surface and calibrate a search before following a hit |
| [Match task content](skills/identify-agents/references/task-content.md) | Compare questions, answers, programs, tables, and source passages |
| [Trace query history](skills/identify-agents/references/query-history.md) | Normalize requests, recover first additions, and compare aligned task state |
| [Assess coordination](skills/identify-agents/references/coordination.md) | Trace complementary work and test ordinary explanations |
| [Recover payloads](skills/identify-agents/references/payloads.md) | Reconstruct encoded fragments and validate the stored object |
| [Search seeds](skills/identify-agents/data/search-seeds.json) | Known positives, ordinary controls, search strings, and provenance |
| [Dataset pins](skills/identify-agents/data/datasets.json) | Versioned sources for task-content comparisons |
| [Task checker](skills/identify-agents/scripts/match_task.py) | Report literal and whitespace-normalized component matches in local text |
| [Investigation note](skills/identify-agents/assets/investigation.md) | Preserve a finding and its next action for continued work |

The guides contain the research needed for their decisions. Historical synthesis
is kept in [research notes](docs/research/2026-09-05/experience.md).
See [release changes](CHANGELOG.md) for corrections and package updates.

## Requirements and checks

Research uses the agent's available public web reader or HTTP tools. The feed
requires no mob account. The optional local checker uses Python's standard
library; run it with UV. Its catalog is a small set of documented seeds, with
external dataset collections linked by revision.

```sh
uv run python -m unittest discover -s tests -v
claude plugin validate . --strict
```

Keep source citations and verification status with catalog updates. Update the
relevant guide when new evidence changes a method, and keep both manifest
versions aligned.
