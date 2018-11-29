class InvalidSource(Exception):
    """Invalid source."""

class UnexpectedCloseParen(Exception):
    """Unexpected ')'."""

class UnexpectedEndOfInput(Exception):
    """Unexpected end of input."""


def tokenize(source):
    spaced = source.replace('(', ' ( ').replace(')', ' ) ')
    return spaced.split()

# ['(', '+', '2', '3', ')']
# ['+', '2', '3', ')']

def parse(tokens):
    assert isinstance(tokens, list)
    head = tokens.pop(0)
    if head == "(":  # s-expression
        ast = []
        while tokens and tokens[0] != ")":
            ast.append(parse(tokens))
        if not tokens:
            raise UnexpectedEndOfSource()
        tokens.pop(0)  # drop ')'
        return ast
    elif head == ')':
        raise UnexpectedCloseParen()
    try:
        return int(head)
    except ValueError:
        return head
