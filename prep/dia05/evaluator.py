import operator


class MissingArgument(Exception):
    """Missing argument."""


class TooManyArguments(Exception):
    """Too many arguments."""


class Operator:
    def __init__(self, arity, function):
        self.arity = arity
        self.function = function

    def __eq__(self, other):
        return self.arity == other.arity and self.function == other.function

    def apply(self, *args):
        if len(args) > self.arity:
            raise TooManyArguments()
        elif len(args) < self.arity:
            raise MissingArgument()
        values = (evaluate(arg) for arg in args)
        return self.function(*values)


BUILTINS = {
    '+': Operator(2, operator.add),
    '-': Operator(2, operator.sub),
    '*': Operator(2, operator.mul),
    '/': Operator(2, operator.floordiv),
    'mod': Operator(2, operator.mod),
    'abs': Operator(1, abs)
}


def evaluate(ast):
    if isinstance(ast, int):
        return ast
    elif isinstance(ast, list):
        op = evaluate(ast[0])
        return op.apply(*ast[1:])

    return BUILTINS[ast]
