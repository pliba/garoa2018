import operator
import collections

import errors


class Form:

    def check_arity(self, args):
        if len(args) > self.arity:
            raise errors.TooManyArguments()
        elif len(args) < self.arity:
            raise errors.MissingArgument()


class Operator(Form):

    def __init__(self, arity, function):
        self.arity = arity
        self.function = function

    def apply(self, *args):
        self.check_arity(args)
        values = (evaluate(arg) for arg in args)
        try:
            return self.function(*values)
        except ZeroDivisionError as exc:
            raise errors.DivisionByZero from exc


class IfStatement(Form):

    arity = 3

    def apply(self, *args):
        self.check_arity(args)
        condition, consequence, alternative = args
        if evaluate(condition):
            return evaluate(consequence)
        else:
            return evaluate(alternative)


class SetStatement(Form):

    arity = 2

    def apply(self, *args):
        self.check_arity(args)
        symbol, expr = args
        value = evaluate(expr)
        global_env[symbol] = value
        return value


class BeginStatement(Form):

    def apply(self, *args):
        for statement in args[:-1]:
            evaluate(statement)
        return evaluate(args[-1])


class WhileStatement(Form):

    arity = 2

    def apply(self, *args):
        self.check_arity(args)
        condition, block = args
        while evaluate(condition):
            evaluate(block)
        return 0


def print_fn(arg):
    print(arg)
    return arg


BUILTINS = {
    '+': Operator(2, operator.add),
    '-': Operator(2, operator.sub),
    '*': Operator(2, operator.mul),
    '/': Operator(2, operator.floordiv),
    '>': Operator(2, operator.gt),
    '<': Operator(2, operator.lt),
    'mod': Operator(2, operator.mod),
    'abs': Operator(1, abs),
    'print': Operator(1, print_fn)
}

SPECIAL_FORMS = {
    'if': IfStatement(),
    'set': SetStatement(),
    'begin': BeginStatement(),
    'while': WhileStatement(),
}

global_vars = {}

global_env = collections.ChainMap(global_vars, SPECIAL_FORMS, BUILTINS)


def evaluate(ast):
    if isinstance(ast, int):
        return ast
    elif isinstance(ast, list):
        op = evaluate(ast[0])
        return op.apply(*ast[1:])

    try:
        return global_env[ast]
    except KeyError as exc:
        raise errors.UnknownSymbol(ast) from exc
