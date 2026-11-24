# Changelog

## v0.4 — 2026-11-24 (proposed)

Separates three layers of trust: approval (mentor), grounding (evidence) and applicability (per query). See `docs/TRUST-LAYERS.md`.

- Added `verification` to the WisdomNode: atomic claims, each with an opaque `evidence_ref` and a status (supported, partially supported, unsupported, unchecked). Now required.
- Replaced `example.firsthand` (boolean) with `example.firsthand_evidence`: `stated_by_mentor`, `corroborated`, `unverified`, `not_firsthand`.
- Release gate: published or agent-retrievable nodes must be fully grounded; partly supported claims need a qualification and human review.
- Unsupported claims must be marked as returned to the mentor.
- Removed `provenance.source_location` so transcript offsets never appear in public records.
- Added `contracts/assessment-response.schema.json` for the applicability verdict: abstain on `does_not_apply`, recommendation-only escalation, required attribution and limits.
- Tests reorganized per contract; 34 checks (5 valid, 29 invalid, one rule each); required text fields must be non-blank.

## v0.3 — 2026-11-23 (proposed)

Changes from the v0.2 candidate schema:

- Added `address` (permanent `leaver/domain.lens[.sub]` format from the Wisdom Marketplace spec).
- Added `mentor` with an opaque `mentor_id`; `display_name` only with name/likeness consent.
- Added `consent` with five separate scopes: record, extract, publish, license, name/likeness.
- `decision_rules` are now typed (rule, threshold, red flag, step).
- Added `example` with a `firsthand` flag, `escalation`, `regulated_domain` and `legal_review`.
- Approval: added `revised` state, mentor-only `decided_by`, `decided_at`; permitted uses are an enumerated list.
- Added the spec's learner fields: `lens`, `visual_spec`, `quiz`.
- Added conditional rules (publish requires approval and consent; regulated domains require clearance).
- Added synthetic examples and a test runner.

## v0.2 — 2026-11-23

Candidate schema prepared in the HAMAL Organization Setup package (not published).
