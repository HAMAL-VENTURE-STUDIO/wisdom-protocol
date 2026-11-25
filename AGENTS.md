# Agent entry: wisdom-protocol

1. This repository is **public**. Never add real mentor data, transcripts, names, consent records or approvals. Examples must be synthetic and say so.
2. Read `README.md`, `docs/TRUST-LAYERS.md` and `CHANGELOG.md` before changing a contract. Keep approval, grounding and applicability separate.
3. Every schema change needs a valid example and, for any new rule, an invalid example that breaks it. `python3 tests/test_schema.py` must pass.
4. The schema is proposed until the founder approves it. Do not describe it as a standard or as adopted by Hanzo.

**Walk Test:** a fresh agent should be able to say when a node may be published, who may approve it, and that no real mentor data lives here.

## Build with Hanzo (HIPs)

HAMAL is part of the Hanzo ecosystem. Before building anything, check the Hanzo Improvement Proposals at https://hips.hanzo.ai and build on the standard that already covers it. Prefer **Final** HIPs; a **Draft** may change. Some HIP numbers appear twice in the listing, so cite a HIP by number **and** title.

Read first: HIP-0119 Service Conventions, HIP-0130 Open-Core Split, HIP-0134 One Process, One Socket, One Identity, HIP-0139 Capability.

| Need | Build on |
| --- | --- |
| Knowledge and memory | HIP-1260 Knowledge (Final); HIP-0522 Context Graph; HIP-0526 Semantic Memory |
| Decisions and verdicts | HIP-1332 Kai (Draft); HIP-0129 Eval (Final) for scoring |
| Tools agents call | HIP-1213 Tool Plane; HIP-0010 / HIP-0300 MCP; HIP-0120 Zap. Expose tools over both MCP and Zap |
| Agents | HIP-1210 Agents; HIP-0009 Agent SDK |
| Skills | HIP-1322 Skills catalogue |
| Identity and permissions | HIP-0111 IAM; HIP-1041 Authz; HIP-1340 Principal |
| Marketplace and payment | HIP-1137 Marketplace; HIP-1335 Listings (Draft); HIP-1163 x402; HIP-1000 Author royalty |
| Tenancy | HIP-0118 Tenant isolation; HIP-0521 Org hierarchy |
| Learning | Hanzo University (white-labelled); HIP-1349 Sensei; HIP-1402 XP |

Do not rebuild what a Final HIP already covers. If nothing covers it, say so in the pull request.

## ICM: how this workspace is organized

This repository follows the Interpretable Context Methodology (ICM): the folder structure *is* the agent architecture.

- **Entry:** this `AGENTS.md` is the root. `CLAUDE.md` only points here.
- **Three primitives:** *sequence* (numbered folders, e.g. `01_inputs/`, run in order, each step's output is the next step's input), *shelf* (unnumbered folders of same-shaped files, e.g. `templates/`), and *catalog* (short index files such as `INDEX.md` that point into folders so agents load only what they need).
- **Every file is one of:** Catalog, Contract (schemas, rules), Factory (prompts, scripts that transform inputs), Product (finished outputs), or Dead (prune or archive it).
- **Stepwise checks:** every sequence step ends with a check (a script, a small model, or a human) before the next step runs.
- **Walk Test:** a fresh agent with no prior memory must be able to read this file, navigate the folders, do its task, and report status from local files alone. Any change must keep the Walk Test passing.
- **Vendor-neutral:** plain Markdown and schemas, readable by any model.
