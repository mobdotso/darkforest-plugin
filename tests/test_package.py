import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_manifests_share_identity_version_and_skills(self):
        codex = json.loads((ROOT / ".codex-plugin/plugin.json").read_text())
        claude = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
        for field in ["name", "version", "description", "author", "repository", "skills"]:
            self.assertEqual(codex[field], claude[field], field)
        self.assertEqual(codex["interface"]["displayName"], claude["displayName"])
        skill_root = (ROOT / codex["skills"]).resolve()
        self.assertTrue(skill_root.is_relative_to(ROOT))
        self.assertTrue(list(skill_root.glob("*/SKILL.md")))

    def test_relative_markdown_links_resolve_inside_package(self):
        for directory in [ROOT / "skills", ROOT / "docs"]:
            for path in directory.rglob("*.md"):
                for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                    if "://" not in target and not target.startswith("#"):
                        resolved = (path.parent / target.split("#")[0]).resolve()
                        self.assertTrue(resolved.is_relative_to(ROOT), (path, target))
                        self.assertTrue(resolved.is_file(), (path, target))

    def test_catalog_ids_and_dataset_references_are_consistent(self):
        data = ROOT / "skills/identify-agents/data"
        seeds = json.loads((data / "search-seeds.json").read_text())["seeds"]
        datasets = json.loads((data / "datasets.json").read_text())["datasets"]
        ids = {dataset["id"] for dataset in datasets}
        self.assertEqual(len(ids), len(datasets))
        self.assertEqual(len({seed["id"] for seed in seeds}), len(seeds))
        for seed in seeds:
            if "dataset_id" in seed:
                self.assertIn(seed["dataset_id"], ids)
            self.assertTrue(seed["report_url"].startswith("https://mob.so/darkforest/p/"))


if __name__ == "__main__":
    unittest.main()
