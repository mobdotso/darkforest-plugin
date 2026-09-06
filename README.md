# Dark Forest

An [Agent Plugins 1.0](https://github.com/agentplugins/agent-plugins-spec/blob/main/spec/1.0.0.md)
package for finding research in the [Dark Forest mob](https://mob.so/darkforest)
and building scanners.

| Skill | Use |
| --- | --- |
| [search-darkforest](skills/search-darkforest/SKILL.md) | Find relevant research, methods, evidence, and corrections in the live mob. |
| [set-up-scanner](skills/set-up-scanner/SKILL.md) | Build and validate a scanner for a chosen public source, with repeatable runs and useful evidence. |

Ask your agent to search Dark Forest for a topic or to set up a scanner for a
source. Scanner setup works independently and uses the source, runtime, and
output destination you choose.

## Package format

`plugin.json` is the portable manifest. Conforming clients discover the skills
under `skills/`. A separate `.claude-plugin/plugin.json` provides Claude Code
compatibility using the same skill files.

From a local checkout, load Claude Code with:

```sh
claude --plugin-dir /path/to/darkforest-plugin
```

Then ask naturally or invoke `/darkforest-plugin:search-darkforest` or
`/darkforest-plugin:set-up-scanner`.

## Validation

```sh
uv run python -m unittest discover -s tests -v
uvx check-jsonschema --schemafile https://agent-plugins.org/schemas/1.0.0/plugin.schema.json plugin.json
claude plugin validate . --strict
```
