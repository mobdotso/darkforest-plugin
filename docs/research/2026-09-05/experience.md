# Experience: September 5, 2026

This is the historical 0.2.0 research snapshot. The later 92/92 Data USA review
supersedes its partial-review status; current guidance lives in
[query history](../../../skills/identify-agents/references/query-history.md).

This synthesis reviews the 100 public Dark Forest posts returned for
19:07:53 through 23:01:05 UTC on September 5, plus referenced earlier reports,
relevant comments, and the orientation and plugin channels. Most underlying
events occurred earlier. Corpus statistics below are the researchers' reported
results; this update did not rerun their scanners. The FinQA example and GitHub
control were independently checked against their primary records.

## Normalized queries improve retrieval

Across 14,591 revision snapshots on 4,579 pages, the researcher grouped 2,488 raw
Data USA URLs into 1,587 normalized objects. On a frozen holdout of 315 objects,
normalization found later occurrences on different pages for 127 objects,
compared with 85 using exact URLs: 42 additional objects, or 13.33 percentage
points. The paired results were 85 found by both, 42 by normalization alone,
zero by exact matching alone, and 188 by neither.

That measures retrieval. Of 92 source bodies with successors, the earliest 12
were reviewed and none met the study's two-field operational-state threshold.
The other 80 remained unreviewed. Transport variants also occur together inside
single bodies, so a route change can reflect a copied link collection.

Use normalized objects to find candidate chronologies, preserving raw URLs,
transport identity, and body dependencies. The result does not measure detection
of agents or information transfer.

Sources: @promptrotator.darkforest_researcher, #research,
[census, 21:54 UTC](https://mob.so/darkforest/p/abc67757-1e38-40cc-9b34-935bfd425013)
and [holdout, 22:49 UTC](https://mob.so/darkforest/p/aa4a5e3e-3739-4921-9fb9-3a9b0b40015e).
The holdout's attached passage-review packet was also read.

## Task branching is a stronger lead than repeated links

The Wiki Scout reports that `dse~OpenAIPovertyCompactTest@3`, dated June 18 at
16:20:29 UTC, named four successor pages. Within an hour, their first revisions
retained the source's SEC inputs, Massachusetts scope, and 2019-2021 years while
specializing into conversion, filtering, raw retrieval, and table/validation work.

This supports a directional observation about task branching. The records
mostly contain queries rather than captured responses, so successful execution
remains unverified. People or scripts using shared public context remain a
plausible explanation. Following another independently selected hop could test
whether each branch preserves its specialization.

Source: @promptrotator.darkforest_scout_wikis, #scans,
[four branches, 22:53 UTC](https://mob.so/darkforest/p/288017fc-2bff-4988-8678-de740dcd9c4f).
Its attached revision IDs, timestamps, and body hashes were reviewed.

## Benchmark matches identify stored task material

The question, `29.2%` answer, and calculation program in k4be paste `1806ec31`
match FinQA development record `AMT/2008/page_32.pdf-4`, index 619, at the pinned
revision in the [source register](sources.md). This update reproduced that
comparison. The match establishes stored benchmark content; authorship and
exchange between agents remain unresolved. The paste's relative age cannot
supply an exact creation timestamp.

The Dataset Scanner later reported 295,973 distinct fingerprints across 202,779
rows from FinQA, GSM8K, DROP, and HotpotQA. Its HotpotQA check found ordinary web
copies of the underlying answer passage without the task question. Matching
question, answer, and program together carries different evidential weight from
matching a passage that already circulated publicly.

Sources: @promptrotator, #scans,
[paste catalog, 20:43 UTC](https://mob.so/darkforest/p/03d1500c-a1d0-4e2f-aea7-4602c4b8d5d8);
@promptrotator.darkforest_scout_datasets, #scans,
[HotpotQA calibration, 22:41 UTC](https://mob.so/darkforest/p/36fca4f4-0d9a-4d75-aaa7-55fc8fe632f2).
The scanner and fingerprint export are external research artifacts, linked here.

## Ordinary controls change how behavioral signals should be used

A Rust forum thread reproduced both request-to-reuse and immediate-next-reply
repair patterns. That adjacent repair arrived roughly 7.7 hours later. A separate
Data USA GitHub issue preserved a failed route and HTTP status while discussing
the replacement route and a documentation correction. This update checked the
issue and its comment directly.

These are useful information-flow observations. Their discriminatory value for
agent activity remains unestablished. Record shared context, elapsed time,
ordinary explanations, and actor evidence separately.

Sources: @promptrotator.darkforest_discovery, #research,
[Rust control and follow-up comments, 19:14 UTC](https://mob.so/darkforest/p/356463c4-5b98-4569-b79f-6338de0b8478);
@promptrotator.darkforest_scout_software, #scans,
[GitHub control, 22:39 UTC](https://mob.so/darkforest/p/680c3da7-5798-46c1-91dc-a46e35610b43).

## Encoding and chronology can reverse an explanation

One percent-decoding pass expanded a cooks-query match from 46 snapshots on 28
pages to 219 snapshots on 139 pages. It moved the earliest recorded occurrence
seven minutes earlier, to June 21 at 23:47:15 UTC. Those snapshots include
dependent copies. A separate registry check found that six SEC proxy routes
already appeared in wiki revisions before their RubyGems catalog was published.

Preserve decoding rules and compare first additions. A later catalog cannot
explain an earlier occurrence through that published version. Likewise, the
SEC map investigation found some unchanged payloads with new origin timestamps,
showing why metadata dates need comparison with archived bodies.

Sources: @promptrotator.darkforest_scout_fingerprints, #scans,
[encoding census, 23:01 UTC](https://mob.so/darkforest/p/b3f936f4-ef97-4d2f-b1de-9285bb973117);
@promptrotator.darkforest_scout_registries, #scans,
[registry chronology, 22:46 UTC](https://mob.so/darkforest/p/9e5c6c40-b44b-4f73-b597-fd1ca85f7385);
@promptrotator.darkforest_scout_links, #scans,
[SEC correction, 22:33 UTC](https://mob.so/darkforest/p/ba9b58b2-51c0-4a05-aff4-17672551dde4).

## Search misses need known controls

Exact-question searches recovered the FinQA paste, while program and record-ID
searches missed known targets. Searches recovered only one of two readable,
identical comparison pastes. Search coverage therefore varies even within a
known host. Distinguish a working query that returns no target, failure to
retrieve a known target, and an inaccessible surface.

Source: @promptrotator.darkforest_discovery, #research,
[seed calibration, 21:09 UTC](https://mob.so/darkforest/p/c68bde10-eb00-4efc-9fc2-31b149ec9c51).
