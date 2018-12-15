from pytest import mark, raises

from parser import tokenize, parse
import errors

@mark.parametrize("source,want", [
    ('a', ['a']),
    ('abs', ['abs']),
    ('(now)', ['(', 'now', ')']),
    ('()', ['(', ')']),
    ('(+ 2   3)', ['(', '+', '2', '3', ')']),
    ('(+ 2 (* 3 5))', ['(', '+', '2', '(', '*', '3', '5', ')', ')']),
])
def test_tokenize(source, want):
    tokens = tokenize(source)
    assert want == tokens


@mark.parametrize("tokens,want", [
    (['2'], 2),
    (['a'], 'a'),
    (['sqrt'], 'sqrt'),
    (['(', 'now', ')'], ['now']),
    (['(', '+', '2', '3', ')'], ['+', 2, 3]),
    (['(', '+', '(', '*', '3', '5', ')', '2', ')'], ['+', ['*', 3, 5], 2]),
    (['(', '+', '2', '(', '*', '3', '5', ')', ')'], ['+', 2, ['*', 3, 5]]),
])
def test_parse(tokens, want):
    ast = parse(tokens)
    assert want == ast


def test_parse_multiple_expressions():
    source = '(+ 1 3) (* 2 4)'
    tokens = tokenize(source)
    ast = parse(tokens)
    want = ['+', 1, 3]
    assert want == ast
    unparsed_tokens = ['(', '*', '2', '4', ')']
    assert unparsed_tokens == tokens


@mark.parametrize("source", [
    '(',
    '(+',
    '(+ 2',
    '(+ 2 (* 3 4)',
])
def test_parse_unexpected_end_of_source(source):
    tokens = tokenize(source)
    with raises(errors.UnexpectedEndOfSource):
        parse(tokens)


@mark.parametrize("source", [
    ')',
])
def test_parse_unexpected_close_paren(source):
    tokens = tokenize(source)
    with raises(errors.UnexpectedCloseParen):
        parse(tokens)
