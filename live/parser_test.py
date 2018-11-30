from pytest import mark

from parser import tokenize, parse

@mark.parametrize("source,want",[
    ('a', ['a']),
    ('abs', ['abs']),
    ('(now)', ['(', 'now', ')']),
    ('()', ['(', ')']),
    ('(+ 2   3)', ['(', '+', '2', '3', ')']),
    ('(+ 2 (* 3 5))', ['(', '+', '2', '(', '*', '3', '5', ')',')']),
])
def test_tokenize(source, want):
    tokens = tokenize(source)
    assert want == tokens


@mark.parametrize("tokens,want",[
    (['2'], 2),
    (['a'], 'a'),
    (['sqrt'], 'sqrt'),
    (['(', 'now', ')'], ['now']),
    (['(', '+', '2', '3', ')'], ['+', 2, 3]),
    (['(', '+', '(', '*', '3', '5', ')', '2', ')'], ['+', ['*', 3, 5], 2]),
    (['(', '+', '2', '(', '*', '3', '5', ')',')'], ['+', 2, ['*', 3, 5]]),
])
def test_parse(tokens, want):
    ast = parse(tokens)
    assert want == ast
