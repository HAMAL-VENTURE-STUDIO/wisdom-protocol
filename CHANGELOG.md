# Changelog

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
