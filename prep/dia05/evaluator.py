import operator

import errors


class Operator:
    def __init__(self, arity, function):
        self.arity = arity
        self.function = function

    def __eq__(self, other):
        return self.arity == other.arity and self.function == other.function

    def apply(self, *args):
        if len(args) > self.arity:
            raise errors.TooManyArguments()
        elif len(args) < self.arity:
            raise errors.MissingArgument()
        values = (evaluate(arg) for arg in args)
        try:
            return self.function(*values)
        except ZeroDivisionError as exc:
            raise errors.DivisionByZero from exc

def if_statement(condition, consequence, alternative):
    return consequence if condition else alternative


BUILTINS = {
    '+': Operator(2, operator.add),
    '-': Operator(2, operator.sub),
    '*': Operator(2, operator.mul),
    '/': Operator(2, operator.floordiv),
    'mod': Operator(2, operator.mod),
    'abs': Operator(1, abs),
    'if': Operator(3, if_statement),
}


def evaluate(ast):
    if isinstance(ast, int):
        return ast
    elif isinstance(ast, list):
        op = evaluate(ast[0])
        return op.apply(*ast[1:])

    return BUILTINS[ast]
