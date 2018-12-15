import errors


def tokenize(source):
    spaced = source.replace('(', ' ( ').replace(')', ' ) ')
    return spaced.split()


def parse(tokens):
    head = tokens.pop(0)
    if head == '(':
        ast = []
        while tokens and tokens[0] != ")":
            ast.append(parse(tokens))
        if not tokens:
            raise errors.UnexpectedEndOfSource()
        tokens.pop(0)  # drop ')'
        return ast
    elif head == ')':
        raise errors.UnexpectedCloseParen()
    try:
        return int(head)
    except ValueError:
        return head
