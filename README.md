# wisdom-protocol

> HAMAL VENTURE STUDIO · Public · Apache-2.0

An open contract for **WisdomNodes**: structured, attributed lessons drawn from people's lived experience, with consent and approval built in, so AI agents can use human judgment without anyone losing ownership of it.

## Status

**Proposed design, v0.3.** The schema is not yet approved by the founder. No real mentor data is in this repository, and none ever will be. All examples are synthetic.

## Why an open contract

The contract is public so developers and the Hanzo ecosystem can integrate with it. The knowledge itself stays private and permission-controlled with each mentor.

## What a WisdomNode holds

| Field | Purpose |
| --- | --- |
| `address` | Permanent address `leaver/domain.lens[.sub]`, e.g. `major/4.10.2` |
| `claim` | The idea in one sentence, in the mentor's words |
| `decision_rules` | Rules, thresholds, red flags or steps an agent acts on |
| `example` | One real case, flagged firsthand or not |
| `boundaries` | When it does not apply, and who should not follow it |
| `context` | Geography, time period, conditions, so agents pick between conflicting mentors by situation instead of averaging them |
| `escalation` | When to hand off to the mentor, a licensed professional or a human reviewer |
| `provenance` | Opaque source reference, location, capture date. Never the transcript itself |
| `consent` | Five separate scopes: record, extract, publish, license, name/likeness |
| `approval` | Mentor-only decision with a record ID and permitted uses |
| `conflicting_node_ids` | Disagreements are kept, not blended |

## Rules the schema enforces

- A node can be **published** only if it is approved **and** publish consent is granted.
- An **approved** node needs a mentor decision with a record ID, date and permitted uses.
- **Only the mentor** can approve their own node.
- A **display name** requires name/likeness consent.
- A published node in a **regulated domain** (finance, health, law) must be legally cleared.

## Run the tests

```bash
pip install jsonschema
python3 tests/test_schema.py
```

Valid examples must pass; each file in `examples/invalid/` breaks one rule and must fail.

## Known limits

- Schema rules cannot prove consent was real; they only refuse records that lack it. Consent records live in access-controlled storage.
- Server-side access and licence terms reduce copying of mentor knowledge; they do not prevent it.

## License

[Apache License 2.0](LICENSE).
