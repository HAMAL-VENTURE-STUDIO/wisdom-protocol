"""Walk Test for the WisdomNode schema.

Every file in examples/valid must pass; every file in examples/invalid must fail.
Run: python3 tests/test_schema.py   (requires: pip install jsonschema)
"""
import json
import pathlib
import sys

from jsonschema import Draft202012Validator, FormatChecker

ROOT = pathlib.Path(__file__).resolve().parent.parent
schema = json.loads((ROOT / "contracts" / "wisdom-node.schema.json").read_text())
Draft202012Validator.check_schema(schema)
validator = Draft202012Validator(schema, format_checker=FormatChecker())

failures = 0
for kind, should_pass in (("valid", True), ("invalid", False)):
    for path in sorted((ROOT / "examples" / kind).glob("*.json")):
        errors = list(validator.iter_errors(json.loads(path.read_text())))
        ok = (not errors) == should_pass
        print(f"{'PASS' if ok else 'FAIL'}  {kind}/{path.name}")
        if not ok:
            failures += 1
            for e in errors[:3]:
                print("      ", e.message)

sys.exit(1 if failures else 0)
