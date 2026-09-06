---
name: set-up-scanner
description: Build or adapt a repeatable scanner that collects public records, applies a detection or matching method, and preserves evidence for review. Use when asked to set up a scanner, add a source adapter, or make an existing scan reliable across repeated runs.
---

# Set up a scanner

Build a working scanner in the user's project. Use their source, detection goal,
runtime, and output destination. This skill applies to public websites, feeds,
repositories, registries, and datasets independently of any community platform.

## Define what a run should establish

Inspect the existing project and reuse its collector, storage, and scheduling
conventions. Identify the record being scanned, the signal sought, and the
evidence needed to review a hit. Clarify missing choices only when they change
the implementation materially.

Choose an observable unit: a post, revision, file, dataset row, or API object.
Distinguish source discovery from reading content and applying the detector.
Record the actual fields a source exposes, including pagination and history.
Prefer documented public APIs or feeds where they provide the required evidence.

## Build one complete path

Implement collection, extraction, matching, and result storage as separable
steps. Keep source-specific parsing in an adapter so another source can reuse
the matcher and storage. Use the project's language and dependencies; use UV
when managing Python packages.

Preserve stable record IDs, source URLs, source timestamps, retrieval times,
and revision or content hashes. Retain the raw record or a durable reference
when needed to explain a match. Extract typed fields such as title, body,
question, table, or source passage rather than flattening away their meaning.
Record parser and matcher versions so results can be reproduced.

Make the detector explain each hit with the matched field, relevant text or
offsets, and the rule that fired. Keep normalization explicit and preserve
the original values. A matching artifact is a candidate for review; any stronger
claim needs the evidence appropriate to the user's detection goal.

## Make repeated runs reliable

Use stable record IDs and revisions or hashes to distinguish new, changed, and
already-seen records. Store checkpoints only after their records are durable.
A repeated run should preserve earlier evidence and avoid duplicate results.
Account for edits and late-arriving records when the source's ordering requires it.

Set request timeouts and respect rate limits and retry delays. Report inaccessible
sources, parsing errors, and incomplete pagination separately from successful
runs with no matches. Preserve the last valid checkpoint after a failed run.
Stream large inputs instead of loading whole collections where size warrants it.

Keep collection and reporting separate. Write to the destination the user chose;
provide a manual run command and integrate the requested schedule using their
existing runner. Keep credentials in the runtime's secret mechanism.

## Validate with evidence

Run a known positive through the complete collection and matching path. Compare
an ordinary or unrelated record to expose overly broad signals. When relevant,
check changed records, duplicate inputs, interrupted pagination, and resumption.
Use saved fixtures to make parser and matcher checks reproducible, alongside a
small live read to verify the source still behaves as expected.

For tuned detection rules, reserve independent records before adjusting the rule.
Measure the relevant unit and denominator: records fetched, bodies parsed,
candidates returned, or confirmed matches. Check component-level recall when a
whole-record representation can hide useful fields.

Deliver the working configuration and code, the manual run command, a sample
result with provenance, the checks performed, and any material coverage limit.
Explain where state lives and how to resume or add another source.
