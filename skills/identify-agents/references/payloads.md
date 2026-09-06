# Recover stored payloads

Use this for numbered pages, encoded blocks, compressed data, or fragments that
may belong to one object.

## Reconstruct as data

Preserve each original body, revision, timestamp, and hash. Identify the proposed
fragment order from explicit numbering or metadata. Inspect raw text and link
targets when rendering may have changed characters. Keep reconstruction steps
and corrected characters alongside the untouched captures.

Join the fragments and decode the recognized encoding. Check compression
integrity and the decoded size and hash. Apply a reasonable output-size limit
when decompressing unknown material. Inspect the result as inert text or data.

Search distinctive decoded rows, labels, or task components. Compare decoded
hashes across sites even when their encodings differ. Move to
[task-content matching](task-content.md) for provenance or
[query history](query-history.md) for first appearance.

## Known reconstruction

The [ProbierWiki investigation](https://mob.so/darkforest/p/4874a674-4b67-430c-97b8-f59268b04830)
joined `OAIIPEDSMay16Map0` through `Map3`, decoded URL-safe base64, and decompressed
gzip to 39,441 bytes. The reported decoded SHA-256 is
`d99db2e828a1080441fc611d5e393844e9fb72327b4443414d79fda6fc761caf`.
The [first page](https://www.wikiservice.at/probier/wiki.cgi?OAIIPEDSMay16Map0)
and the report's remaining links are starting points; live pages can change.

Wiki rendering had displayed underscores as spaces while link targets retained
the original characters. Some archive views contained placeholders although
live pages retained the payload. Specify which representation you inspected.

A valid reconstruction establishes one storage workflow. Validate row meanings
and values against their source before describing the dataset, and assess the
number of agents separately from the number of fragments or IP labels.
