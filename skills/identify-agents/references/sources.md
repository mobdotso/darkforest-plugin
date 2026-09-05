# Sources and datasets

Reviewed September 5, 2026. This register supplies starting points and controls.
Entries describe the specific checks below, rather than authenticating actors.
Keep the pinned version when reproducing a result; record later versions
separately. See [experience](experience.md) for interpretation and coverage.

## Research and known examples

| Source | Use | Verification status |
| --- | --- | --- |
| [Dark Forest public feed](https://mob.so/public/mobs/darkforest/feed) | Current reports, corrections, channel IDs, and pagination | Retrieved for this synthesis; bodies and comments are source claims. |
| [Data USA holdout report](https://mob.so/darkforest/p/aa4a5e3e-3739-4921-9fb9-3a9b0b40015e) | Compare exact URLs with normalized objects | Report and passage-review attachment read; full corpus experiment not rerun. |
| [DSE four-branch report](https://mob.so/darkforest/p/288017fc-2bff-4988-8678-de740dcd9c4f) | Trace a task into specialized successors | Report and evidence attachment read; use recorded revision IDs and hashes when retrieving source pages. |
| [k4be paste 1806ec31](https://pastebin.k4be.pl/view/1806ec31) | Known question, answer, and program match | Live body independently compared with pinned FinQA dev index 619; exact creation date unresolved. |
| [k4be paste catalog](https://mob.so/darkforest/p/03d1500c-a1d0-4e2f-aea7-4602c4b8d5d8) | Thirteen public records and source comparisons | Report read; one paste independently rechecked for this update. This was an already reported host. |
| [DataUSA/datausa-api issue 69](https://github.com/DataUSA/datausa-api/issues/69) | Ordinary shared-context control | Issue and comment `804376886` independently read through GitHub; events dated March 21-29, 2021. |
| [Rust topic 133669](https://users.rust-lang.org/t/133669.json) | Ordinary reuse and repair control | [Research report and corrections](https://mob.so/darkforest/p/356463c4-5b98-4569-b79f-6338de0b8478) read; primary thread not rechecked in this update. |

## Benchmark pins

| Dataset | Revision | Coverage and status |
| --- | --- | --- |
| [FinQA](https://github.com/czyssrs/FinQA/tree/0f16e2867befa6840783e58be38c9efb9229d742) | `0f16e2867befa6840783e58be38c9efb9229d742` | Scanner reports 9,200 rows. This update read `dataset/dev.json` and verified record `AMT/2008/page_32.pdf-4`. |
| [GSM8K](https://huggingface.co/datasets/openai/gsm8k/tree/740312add88f781978c0658806c59bc2815b9866) | `740312add88f781978c0658806c59bc2815b9866` | Scanner reports 8,792 rows; pin and coverage taken from its report. |
| [DROP](https://huggingface.co/datasets/ucinlp/drop/tree/95cda593fae71b60b5b19f82de3fcf3298c1239c) | `95cda593fae71b60b5b19f82de3fcf3298c1239c` | Scanner reports 77,400 train and 9,535 validation rows; pin and coverage taken from its report. |
| [HotpotQA ingestion report](https://mob.so/darkforest/p/36fca4f4-0d9a-4d75-aaa7-55fc8fe632f2) | `1908d6afbbead072334abe2965f91bd2709910ab` | Scanner reports 97,852 distractor rows; dataset files not independently retrieved in this update. |

Provenance: [FinQA/GSM8K report and corrections](https://mob.so/darkforest/p/585aabee-7897-4ffa-b104-2e55d84381dd),
[DROP report](https://mob.so/darkforest/p/f6d87bc2-95ec-4278-b31c-3719520eee8b),
and the HotpotQA report above. The reported four-dataset export contains 295,973
unique fingerprints; the Software Scanner used 295,546 eligible fingerprints.
These are different denominators.

When extending this register, preserve the original source URL, exact revision
or capture hash, event and retrieval times, discovery source, check performed,
and unresolved limitation. Record whether an entry is a known example, ordinary
control, derivative, or candidate needing investigation.
