import operator

from pytest import mark, raises

from evaluator import evaluate, Operator
from parser import tokenize, parse

import errors


def test_evaluate_integer():
    ast = 2
    want = 2
    got = evaluate(ast)
    assert want == got


def test_evaluate_symbol():
    ast = '*'
    want = Operator(2, operator.mul)
    got = evaluate(ast)
    assert want.arity == got.arity
    assert want.function == got.function


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
    with raises(errors.MissingArgument):
        evaluate(ast)


def test_evaluate_excess_arg():
    source = '(mod 2 3 4)'
    ast = parse(tokenize(source))
    with raises(errors.TooManyArguments):
        evaluate(ast)


def test_evaluate_excess_arg2():
    source = '(abs -2 3)'
    ast = parse(tokenize(source))
    with raises(errors.TooManyArguments):
        evaluate(ast)


def test_evaluate_multiple_lines():
    source = '(+ 2 3)\n(* 2 3)'
    want = [5, 6]
    tokens = tokenize(source)
    while tokens:
        ast = parse(tokens)
        got = evaluate(ast)
        assert want.pop(0) == got


def test_evaluate_division_by_zero():
    source = '(/ 1 0)'
    ast = parse(tokenize(source))
    with raises(errors.DivisionByZero):
        evaluate(ast)


def test_evaluate_unknown_function():
    source = '($ 1 2)'
    ast = parse(tokenize(source))
    with raises(errors.UnknownSymbol):
        evaluate(ast)
       

@mark.parametrize("source,want", [
    ('(if 1 1 2)', 1),
    ('(if 0 1 2)', 2),
    ('(if (> 1 0) 1 (/ 1 0))', 1),
])
def test_evaluate_if(source, want):
    ast = parse(tokenize(source))
    got = evaluate(ast)
    assert want == got


def test_evaluate_set():
    source = '(set x 3)\n(* 2 x)'
    want = [3, 6]
    tokens = tokenize(source)
    while tokens:
        ast = parse(tokens)
        got = evaluate(ast)
        assert want.pop(0) == got


def test_print(capsys):
    ast = parse(tokenize('(print 7)'))
    got = evaluate(ast)
    assert 7 == got
    captured = capsys.readouterr()
    assert '7\n' == captured.out


def test_begin(capsys):
    source = """
    (begin
        (print 1)
        (print 2)
        (print 3)
    )
    """
    ast = parse(tokenize(source))
    got = evaluate(ast)
    assert 3 == got
    captured = capsys.readouterr()
    assert '1\n2\n3\n' == captured.out


@mark.parametrize("source,out", [
    ('(while 0 (print 1))', ''),
    ("""(begin
           (set x 2)
           (while x (begin
              (print x)
              (set x (- x 1))
           ))
        )""", '2\n1\n'),
])
def test_while(capsys, source, out):
    ast = parse(tokenize(source))
    got = evaluate(ast)
    assert 0 == got
    captured = capsys.readouterr()
    assert out == captured.out
