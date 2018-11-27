import collections

class InvalidSource(Exception):
    """Invalid source."""

class UnexpectedCloseParen(Exception):
    """Unexpected ')'."""

class UnexpectedEndOfInput(Exception):
    """Unexpected end of input."""


def tokenize(source):
    spaced = source.replace('(', ' ( ').replace(')', ' ) ')
    return collections.deque(spaced.split())


def parse(tokens):
    "Construir AST (expressões aninhadas)"
    head = tokens.popleft()
    if head == "(":  # s-expression
        ast = []
        while tokens and tokens[0] != ")":
            ast.append(parse(tokens))
        tokens.popleft()  # descartar ')'
        return ast
    elif head == ')':
        raise UnexpectedCloseParen()
    try:
        return int(head)  # número
    except ValueError:
        return head  # símbolo
