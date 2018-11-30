import operator
import collections

class MissingArgument(Exception):
    """Missing argument."""

class TooManyArguments(Exception):
    """Too many arguments."""

Operator = collections.namedtuple('Operator', 'arity function')

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
        len_args = len(ast[1:])
     
        if len_args > op.arity:
            raise TooManyArguments()
        elif len_args < op.arity:
            raise MissingArgument()
     
        args = (evaluate(arg) for arg in ast[1:])
        return op.function(*args)

    return BUILTINS[ast]
