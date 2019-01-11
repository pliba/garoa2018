def tokenize(source):
    spaced = source.replace('(', ' ( ').replace(')', ' ) ')
    return spaced.split()


OPERATORS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}

def evaluate(tokens):
    head = tokens.pop(0)
    if head == '(':
        op = OPERATORS[tokens.pop(0)]
        args = []
        while tokens and tokens[0] != ")":
            args.append(evaluate(tokens))
        tokens.pop(0)  # drop ')'
        return op(*args)
    else:
        return float(head)
