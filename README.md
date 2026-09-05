# Dark Forest

An OpenAI plugin for discovering AI agents and agent swarms.

| Skill | Purpose |
| --- | --- |
| [read-darkforest](skills/read-darkforest/SKILL.md) | Read and summarize the public [Dark Forest mob](https://mob.so/darkforest) through unauthenticated requests. |
| [identify-agents](skills/identify-agents/SKILL.md) | Identify likely agent activity and assess evidence of coordination. |

Each skill lives under `skills/<name>/SKILL.md`. Findings explain the evidence,
alternative explanations, and limits of attribution.

## Research library

The September 5, 2026 update turns recent Dark Forest investigations into
references that people and agents can use:

- [Experience](skills/identify-agents/references/experience.md): findings,
  corrections, and what the evidence supports.
- [Sources and datasets](skills/identify-agents/references/sources.md): pinned
  datasets, known examples, comparison cases, and verification status.
- [Strategy](skills/identify-agents/references/strategy.md): finding task
  material, reconstructing chronology, and testing coordination hypotheses.

The strongest measured improvement is in candidate retrieval: normalized
Data USA queries found later occurrences for 127 of 315 held-out objects,
compared with 85 using exact URLs. Ordinary discussions also reproduced
proposed behavioral signals, so information reuse and actor attribution
need separate assessments.

The manifest lives at `.codex-plugin/plugin.json` and follows the
[OpenAI plugin format](https://developers.openai.com/plugins/build/plugins#plugin-structure).
