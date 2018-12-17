import operator

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


BUILTINS = {
    '+': Operator(2, operator.add),
    '-': Operator(2, operator.sub),
    '*': Operator(2, operator.mul),
    '/': Operator(2, operator.floordiv),
    '>': Operator(2, operator.gt),
    '<': Operator(2, operator.lt),
    'mod': Operator(2, operator.mod),
    'abs': Operator(1, abs),
}

SPECIAL_FORMS = {
    'if': IfStatement(),
}

def evaluate(ast):
    if isinstance(ast, int):
        return ast
    elif isinstance(ast, list):
        op = evaluate(ast[0])
        return op.apply(*ast[1:])

    try:
        return SPECIAL_FORMS[ast]
    except KeyError:
        return BUILTINS[ast]
