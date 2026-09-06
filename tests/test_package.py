import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_portable_manifest_and_claude_compatibility_share_identity(self):
        portable = json.loads((ROOT / "plugin.json").read_text())
        claude = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
        self.assertEqual(portable["$schema"],
                         "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json")
        for field in ["name", "version", "description", "author", "repository"]:
            self.assertEqual(portable[field], claude[field], field)
        self.assertEqual((ROOT / claude["skills"]).resolve(), ROOT / "skills")

    def test_claude_mcp_adapter_matches_portable_servers(self):
        portable = json.loads((ROOT / "mcp.json").read_text())
        native = json.loads((ROOT / ".mcp.json").read_text())
        self.assertEqual(portable["$schema"],
                         "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json")
        self.assertEqual(portable["mcpServers"].keys(), native["mcpServers"].keys())
        for name, server in portable["mcpServers"].items():
            self.assertEqual(server["type"], "streamable-http")
            adapted = dict(server, type="http")
            self.assertEqual(adapted, native["mcpServers"][name])

    def test_skills_are_discoverable_inside_package(self):
        skills = list((ROOT / "skills").glob("*/SKILL.md"))
        self.assertTrue(skills)
        for skill in skills:
            self.assertTrue(skill.resolve().is_relative_to(ROOT))
            self.assertTrue(skill.is_file())
            self.assertTrue(skill.read_text().startswith("---\n"))

    def test_relative_markdown_links_resolve_inside_package(self):
        files = [ROOT / "README.md", *(ROOT / "skills").rglob("*.md"),
                 *(ROOT / "docs").rglob("*.md")]
        for path in files:
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if "://" not in target and not target.startswith("#"):
                    resolved = (path.parent / target.split("#")[0]).resolve()
                    self.assertTrue(resolved.is_relative_to(ROOT), (path, target))
                    self.assertTrue(resolved.is_file(), (path, target))


if __name__ == "__main__":
    unittest.main()
