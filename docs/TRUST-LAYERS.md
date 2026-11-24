# Three layers of trust

**Status:** proposed design, v0.4.

A WisdomNode carries one person's lived experience. Three different questions decide whether an AI agent may use it, and each is answered by a different party at a different time. Keeping them separate is the core of the protocol.

| Layer | Question | Decided by | When | Where it lives |
| --- | --- | --- | --- | --- |
| **1. Approval** | Does this node faithfully represent my experience and the lesson I intend? | The mentor, and only the mentor | Once per node version | `approval` on the node |
| **2. Grounding** | Does the source support each claim? What backs the account of firsthand experience? | Automated checks with human review | Once per node version | `verification` and `example.firsthand_evidence` on the node |
| **3. Applicability** | Does this lesson fit the situation the agent is asking about? | The system, at query time | Every `assess` call | `assessment-response.schema.json`, never on the node |

## What none of the layers does

No layer certifies that a lesson is true for everyone. Grounding confirms that the mentor said and meant what the node claims. Two mentors who disagree can both be fully grounded; the protocol keeps both views (`conflicting_node_ids`, `conflicting_views`) and lets context decide which applies.

## Grounding rules

- Each node is broken into small, checkable statements (`verification.claims`). Each statement points to its evidence through an **opaque** reference. Exact transcript offsets stay in secure storage and never appear in a public record.
- Each statement is `supported`, `partially_supported`, `unsupported`, or `unchecked`.
- **Release gate.** A node that is published, or whose approved uses include agent retrieval, must have grounding `complete`, at least one checked statement, and no `unsupported` or `unchecked` statements.
- **Partly supported statements** may be released only with a written `qualification` and `human_reviewed: true`. Agents must pass the qualification on (in `limits`), so the unsupported part is never presented as established.
- **Unsupported statements** go back to the mentor (`returned_to_mentor: true`). They are never silently deleted.
- **Firsthand evidence** has four values: `stated_by_mentor` (the mentor says they lived it, which is not proof), `corroborated`, `unverified`, `not_firsthand`.

## Applicability rules

- `applies`: credit at least one node, name the rules that triggered, do not abstain.
- `partly_applies`: as above, plus `limits` saying what the lesson does not cover.
- `does_not_apply`: abstain. No rules, no next steps, and recommend escalation with a target and a reason.
- Escalation is a **recommendation only** (`auto_contact: false`). The system never books or contacts a person on its own.
- The response carries verdicts and triggered rules, never the node's full text, and only grounded content (`presents_only_grounded_content: true`).

## Relation to HIP-1346

Grounding uses the same idea as Hanzo HIP-1346 Bounty #30 (atomic factuality verification): break an answer into atomic claims linked to evidence spans and measure how many are supported. A Pilot 000 evaluation harness built on these contracts can report the same metrics.
