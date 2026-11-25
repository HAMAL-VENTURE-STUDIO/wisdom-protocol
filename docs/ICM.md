# ICM: how this workspace is organized

This repository follows the Interpretable Context Methodology (ICM): the folder structure *is* the agent architecture.

ICM was created by Jake Van Clief and David McDermott ("Interpretable Context Methodology: Folder Structure as Agentic Architecture", arXiv:2603.16021, 2026), and is open source under the MIT license: https://github.com/RinDig/Interpretable-Context-Methodology-ICM. HAMAL applies ICM to its agents; credit the authors when describing it.

- **Entry:** `AGENTS.md` is the root and only routes; it holds no content. `CLAUDE.md` only points here.
- **Three primitives:** *sequence* (numbered folders, e.g. `01_inputs/`, run in order, each step's output is the next step's input), *shelf* (unnumbered folders of same-shaped files, e.g. `templates/`), and *catalog* (short index files such as `INDEX.md` that point into folders so agents load only what they need).
- **Every file is one of:** Catalog, Contract (schemas, rules), Factory (prompts, scripts that transform inputs), Product (finished outputs), or Dead (prune or archive it).
- **Stepwise checks:** every sequence step ends with a check (a script, a small model, or a human) before the next step runs.
- **Walk Test:** a fresh agent with no prior memory must be able to read this file, navigate the folders, do its task, and report status from local files alone. Any change must keep the Walk Test passing.
- **Vendor-neutral:** plain Markdown and schemas, readable by any model.

- **Folder contracts:** every working folder has a `CONTEXT.md` saying what it reads, what it does, what it writes, and how it is checked.
- **Link check:** `python -I _tools/links.py .` must pass (runs in CI).
