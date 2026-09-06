import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/identify-agents/scripts/match_task.py"
spec = importlib.util.spec_from_file_location("match_task", SCRIPT)
matcher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(matcher)
SEEDS = json.loads(matcher.DEFAULT_CATALOG.read_text())["seeds"]
TASK = next(seed for seed in SEEDS if seed["id"] == "finqa-amt-2008")
PASSAGE = next(seed for seed in SEEDS if seed["id"] == "hotpotqa-upstream-sentence")


class TaskMatchingTests(unittest.TestCase):
    def test_complete_task_has_literal_component_offsets(self):
        text = "\n".join(TASK["components"].values())
        result = matcher.match_components(text, [TASK])[0]
        for component in result["components"]:
            self.assertEqual(component["match"], "literal")
            offset = component["literal_character_offsets"][0]
            self.assertEqual(text[offset:offset + len(component["value"])], component["value"])

    def test_whitespace_change_is_reported_separately(self):
        text = TASK["components"]["question"].replace(" ", "\n  ")
        components = matcher.match_components(text, [TASK])[0]["components"]
        self.assertEqual(components[0]["match"], "whitespace_normalized")
        self.assertEqual(components[0]["literal_character_offsets"], [])
        self.assertEqual([c["match"] for c in components[1:]], ["absent", "absent"])

    def test_upstream_sentence_stays_a_passage_control(self):
        result = matcher.match_components(PASSAGE["components"]["source_passage"], [TASK, PASSAGE])
        self.assertTrue(all(c["match"] == "absent" for c in result[0]["components"]))
        self.assertEqual(result[1]["role"], "upstream_content_control")
        self.assertEqual(result[1]["components"][0]["component"], "source_passage")
        self.assertEqual(result[1]["components"][0]["match"], "literal")

    def test_unrelated_text_has_no_match(self):
        result = matcher.match_components("A routine maintenance note.", [TASK, PASSAGE])
        self.assertTrue(all(c["match"] == "absent" for r in result for c in r["components"]))

    def test_cli_resolves_catalog_from_another_working_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "page.txt"
            path.write_text(TASK["components"]["program"])
            result = subprocess.run([sys.executable, str(SCRIPT), str(path), "--seed", TASK["id"]],
                                    cwd=directory, text=True, capture_output=True, check=True)
            report = json.loads(result.stdout)
            self.assertEqual([c["match"] for c in report["results"][0]["components"]],
                             ["absent", "absent", "literal"])
            self.assertEqual(report["results"][0]["record_id"], TASK["record_id"])

    def test_control_without_components_is_an_explicit_error(self):
        result = subprocess.run([sys.executable, str(SCRIPT), str(SCRIPT), "--seed", "rust-ordinary-reuse"],
                                text=True, capture_output=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("No component seed", result.stderr)

    def test_empty_component_cannot_match_everything(self):
        with self.assertRaises(ValueError):
            matcher.match_components("anything", [{"id": "invalid", "components": {"question": " "}}])


if __name__ == "__main__":
    unittest.main()
