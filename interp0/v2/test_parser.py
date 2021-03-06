from pytest import mark, raises

from parser import tokenize, parse
import errors


@mark.parametrize("source,want", [
    ("3", ["3"]),
    ("(+ 2 3)", ["(", "+", "2", "3", ")"]),
    ("(+ 2 (* 3 4))", ["(", "+", "2", "(", "*", "3", "4", ")", ")"]),
])
def test_tokenize(source, want):
    assert want == tokenize(source)


@mark.parametrize("tokens,want", [
    (["3"], 3),
    (["-3"], -3),
    (["+3"], 3),
    (["+"], "+")
])
def test_parse_atoms(tokens, want):
    assert want == parse(tokens)


def test_parse_no_source():
    with raises(errors.UnexpectedEndOfSource):
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
    with raises(errors.UnexpectedEndOfSource):
        parse(["("])


def test_parse_unexpected_close_paren():
    with raises(errors.UnexpectedCloseParen):
        parse([")"])


def test_parse_unexpected_close_paren_message():
    with raises(errors.UnexpectedCloseParen) as excinfo:
        parse([")"])

    assert str(excinfo.value) == "Unexpected ')'."
