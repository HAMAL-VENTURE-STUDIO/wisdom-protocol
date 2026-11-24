"""Walk Test for the Wisdom Protocol contracts.

For each contract in contracts/, every file in examples/<contract>/valid must pass
and every file in examples/<contract>/invalid must fail. Each invalid file breaks
exactly one rule, named by its filename.

Run: python3 tests/test_schema.py   (requires: pip install "jsonschema>=4.18")
"""
import json
import pathlib
import sys

from jsonschema import Draft202012Validator, FormatChecker

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTRACTS = {
    "wisdom-node": "wisdom-node.schema.json",
    "assessment-response": "assessment-response.schema.json",
}

failures = 0
for name, filename in CONTRACTS.items():
    schema = json.loads((ROOT / "contracts" / filename).read_text())
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    print(f"== {name}")
    for kind, should_pass in (("valid", True), ("invalid", False)):
        files = sorted((ROOT / "examples" / name / kind).glob("*.json"))
        if not files:
            print(f"FAIL  no {kind} examples for {name}")
            failures += 1
        for path in files:
            errors = list(validator.iter_errors(json.loads(path.read_text())))
            ok = (not errors) == should_pass
            print(f"{'PASS' if ok else 'FAIL'}  {kind}/{path.name}")
            if not ok:
                failures += 1
                for e in errors[:3]:
                    print("      ", e.message)

print(f"\n{'All checks passed.' if not failures else f'{failures} check(s) failed.'}")
sys.exit(1 if failures else 0)
