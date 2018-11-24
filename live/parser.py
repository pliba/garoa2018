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
    if head == '(':
        if tokens[-1] == ')':
            tokens = tokens[:-1]
        else:
            raise UnexpectedEndOfInput()
        ast = []
        for token in tokens:
            if token == ')':
                break
            ast.append(parse(tokens))
        return ast
    elif head == ')':
        raise UnexpectedCloseParen()
    try:
        return int(head)
    except ValueError:
        return head
