from pytest import mark, raises

from parser import tokenize, parse
from parser import UnexpectedEndOfInput


@mark.parametrize("source,want", [
    ("3", ["3"]),
    ("(+ 2 3)", ["(", "+", "2", "3", ")"]),
    ("(+ 2 (* 3 4))", ["(", "+", "2", "(", "*", "3", "4", ")", ")"]),
])
def test_tokenize(source, want):
    assert tokenize(source) == want


@mark.parametrize("tokens,want", [
    (["3"], 3),
    (["-3"], -3),
    (["+3"], 3),
    (["+"], "+"),
])
def test_parse_atoms(tokens, want):
    assert parse(tokens) == want


def test_parse_no_source():
    with raises(UnexpectedEndOfInput):
        parse([])


@mark.parametrize("source,want", [
    ("(2)", [2]),
    ("(+ 2 3)", ["+", 2, 3]),
    ("(+ 2 (* 3 4))", ["+", 2, ["*", 3, 4]]),
])
def test_parse_expressions(source, want):
    tokens = tokenize(source)
    assert parse(tokens) == want
