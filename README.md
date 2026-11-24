# wisdom-protocol

> HAMAL VENTURE STUDIO · Public · Apache-2.0

An open contract for **WisdomNodes**: structured, attributed lessons drawn from people's lived experience, with consent and approval built in, so AI agents can use human judgment without anyone losing ownership of it.

## Status

**Proposed design, v0.4.** The schema is not yet approved by the founder. No real mentor data is in this repository, and none ever will be. All examples are synthetic.

## Why an open contract

The contract is public so developers and the Hanzo ecosystem can integrate with it. The knowledge itself stays private and permission-controlled with each mentor.

## Three layers of trust

| Layer | Question | Decided by | Where |
| --- | --- | --- | --- |
| Approval | Does this represent my experience? | The mentor | On the node, once per version |
| Grounding | Does the source support each claim? | Automated checks + human review | On the node, once per version |
| Applicability | Does it fit this situation? | The system, per query | `assessment-response.schema.json` |

None of these certifies a lesson as universally true. See [`docs/TRUST-LAYERS.md`](docs/TRUST-LAYERS.md).

## Contracts

- [`contracts/wisdom-node.schema.json`](contracts/wisdom-node.schema.json): the WisdomNode
- [`contracts/assessment-response.schema.json`](contracts/assessment-response.schema.json): what an agent gets back from an `assess` call

## What a WisdomNode holds

| Field | Purpose |
| --- | --- |
| `address` | Permanent address `leaver/domain.lens[.sub]`, e.g. `major/4.10.2` |
| `claim` | The idea in one sentence, in the mentor's words |
| `decision_rules` | Rules, thresholds, red flags or steps an agent acts on |
| `example` | One real case, with what backs the firsthand account (`stated_by_mentor`, `corroborated`, `unverified`, `not_firsthand`) |
| `boundaries` | When it does not apply, and who should not follow it |
| `context` | Geography, time period, conditions, so agents pick between conflicting mentors by situation instead of averaging them |
| `escalation` | When to hand off to the mentor, a licensed professional or a human reviewer |
| `provenance` | Opaque source reference and capture date. Never the transcript or transcript offsets |
| `verification` | Grounding: the node broken into checkable claims, each linked to evidence and marked supported, partly supported, unsupported or unchecked |
| `consent` | Five separate scopes: record, extract, publish, license, name/likeness |
| `approval` | Mentor-only decision with a record ID and permitted uses |
| `conflicting_node_ids` | Disagreements are kept, not blended |

## Rules the schema enforces

- A node can be **published** only if it is approved **and** publish consent is granted.
- An **approved** node needs a mentor decision with a record ID, date and permitted uses.
- **Only the mentor** can approve their own node.
- A **display name** requires name/likeness consent.
- A published node in a **regulated domain** (finance, health, law) must be legally cleared.
- **Release gate:** a node released to agents or published must be fully grounded: no unsupported or unchecked claims, and partly supported claims only with a written qualification and human review.
- Unsupported claims are **returned to the mentor**, never silently deleted.

## Rules the assessment response enforces

- `does_not_apply` means **abstain**: no advice, and an escalation recommendation with a target and reason.
- Escalation never contacts a person automatically (`auto_contact: false`).
- A fit or partial fit must credit the nodes used; a partial fit must state its limits.
- Responses never include a node's full text, and only draw on grounded content.

## Run the tests

```bash
pip install jsonschema
python3 tests/test_schema.py
```

Each contract has `examples/<contract>/valid/` (must pass) and `examples/<contract>/invalid/` (each file breaks exactly one rule, named by its filename, and must fail).

## Known limits

- Schema rules cannot prove consent was real; they only refuse records that lack it. Consent records live in access-controlled storage.
- Server-side access and licence terms reduce copying of mentor knowledge; they do not prevent it.

## License

[Apache License 2.0](LICENSE).
