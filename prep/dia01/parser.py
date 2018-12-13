class UnexpectedCloseParen(Exception):
    """Unexpected ')'."""


def tokenize(source):
    spaced = source.replace('(', ' ( ').replace(')', ' ) ')
    return spaced.split()


def parse(tokens):
    assert isinstance(tokens, list)
    head = tokens.pop(0)
    if head == '(':
        ast = []
        while tokens[0] != ')':
            ast.append(parse(tokens))
        tokens.pop(0)  # drop ')'
        return ast
    elif head == ')':
        raise UnexpectedCloseParen()
    try:
        return int(head)
    except ValueError:
        return head
