import operator

from pytest import mark, raises

from evaluator import evaluate, Operator
from evaluator import MissingArgument, TooManyArguments
from parser import tokenize, parse


def test_evaluate_integer():
    ast = 2
    want = 2
    got = evaluate(ast)
    assert want == got


def test_evaluate_symbol():
    ast = '*'
    want = Operator(2, operator.mul)
    got = evaluate(ast)
    assert want == got


@mark.parametrize("source,want", [
    ('(* 2 3)', 6),
    ('(* 2 (* 3 4))', 24),
    # (100°F − 32) * 5 / 9 = 37°C
    ("(/ (* (- 100 32) 5) 9)", 37),
    ('(mod 8 3)', 2),
])
def test_evaluate_expr(source, want):
    ast = parse(tokenize(source))
    got = evaluate(ast)
    assert want == got


def test_evaluate_missing_arg():
    source = '(* 2)'
    ast = parse(tokenize(source))
    with raises(MissingArgument):
        evaluate(ast)


def test_evaluate_excess_arg():
    source = '(mod 2 3 4)'
    ast = parse(tokenize(source))
    with raises(TooManyArguments):
        evaluate(ast)


def test_evaluate_excess_arg2():
    source = '(abs -2 3)'
    ast = parse(tokenize(source))
    with raises(TooManyArguments):
        evaluate(ast)


def test_evaluate_multiple_lines():
    source = '(+ 2 3)\n(* 2 3)'
    want = [5, 6]
    tokens = tokenize(source)
    while tokens:
        ast = parse(tokens)
        got = evaluate(ast)
        assert want.pop(0) == got
