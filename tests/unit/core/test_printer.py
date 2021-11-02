import json

from tests.unit.conftest import fixture_path
from whispers.core.args import parse_args
from whispers.core.printer import printer
from whispers.models.pair import KeyValuePair


def test_printer(tmp_path, rule_fixture):
    tmp = tmp_path.joinpath("printer.test")
    args = parse_args(["-o", tmp.as_posix(), fixture_path()])
    pair = KeyValuePair("key", "value", ["root", "key"], "/file", 123, rule_fixture)

    assert json.loads(printer(args, pair)) == {
        "key": pair.key,
        "value": pair.value,
        "file": pair.file,
        "line": pair.line,
        "rule_id": pair.rule.id,
        "message": pair.rule.message,
        "severity": pair.rule.severity,
    }
