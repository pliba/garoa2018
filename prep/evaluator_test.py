import operator

from pytest import mark

from parser import parse, tokenize
from evaluator import evaluate, Operator

@mark.parametrize("source,want", [
    ("2", 2),
    ("-2", -2)
])
def test_evaluate_number_literals(source, want):
    expr = parse(tokenize(source))
    assert want == evaluate(expr)


def test_evaluate_builtin():
    expr = parse(tokenize("+"))
    want = Operator(symbol="+", function=operator.add)
    assert want == evaluate(expr)


@mark.parametrize("source,want", [
    ("(+ 1 2)", 3),
    ("(* 3 (+ 4 5))", 27),
    # (100°F − 32) * 5 / 9 = 37°C
    ("(/ (* (- 100 32) 5) 9)", 37),
])
def test_evaluate_s_expressions(source, want):
    expr = parse(tokenize(source))
    assert want == evaluate(expr)
