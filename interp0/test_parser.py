from pytest import mark, raises

from parser import tokenize, parse
from parser import UnexpectedEndOfInput, UnexpectedCloseParen


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
    ("(+ (* 2  3) (- 4 5))", ["+", ["*", 2, 3], ["-", 4, 5]]),
])
def test_parse_expressions(source, want):
    tokens = tokenize(source)
    assert want == parse(tokens)


def test_parse_no_close_paren():
    with raises(UnexpectedEndOfInput):
        parse(["("])

def test_parse_unexpected_close_paren():
    with raises(UnexpectedCloseParen):
        parse([")"])

def test_parse_unexpected_close_paren_message():
    with raises(UnexpectedCloseParen) as excinfo:
        parse([")"])
    assert str(excinfo.value) == "Unexpected ')'."
