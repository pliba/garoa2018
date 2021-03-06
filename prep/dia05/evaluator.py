import operator
import collections

import errors


# ______________________________________ Built-in functions


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

    def apply(self, environment, *args):
        self.check_arity(args)
        values = (evaluate(arg, environment) for arg in args)
        return self.function(*values)


def print_fn(arg):
    print(arg)
    return arg


BUILTINS = {
    '+': Operator(2, operator.add),
    '-': Operator(2, operator.sub),
    '*': Operator(2, operator.mul),
    '/': Operator(2, operator.floordiv),
    '=': Operator(2, operator.eq),
    '>': Operator(2, operator.gt),
    '<': Operator(2, operator.lt),
    'mod': Operator(2, operator.mod),
    'abs': Operator(1, abs),
    'print': Operator(1, print_fn)
}


# ______________________________________ Special forms


class IfStatement(Form):

    arity = 3

    def apply(self, environment, *args):
        self.check_arity(args)
        condition, consequence, alternative = args
        if evaluate(condition, environment):
            return evaluate(consequence, environment)
        else:
            return evaluate(alternative, environment)


class BeginStatement(Form):

    def apply(self, environment, *args):
        for statement in args[:-1]:
            evaluate(statement, environment)
        return evaluate(args[-1], environment)


class WhileStatement(Form):

    arity = 2

    def apply(self, environment, *args):
        self.check_arity(args)
        condition, block = args
        while evaluate(condition, environment):
            evaluate(block, environment)
        return 0


class SetStatement(Form):

    arity = 2

    def apply(self, environment, *args):
        self.check_arity(args)
        symbol, expr = args
        value = evaluate(expr, environment)
        environment[symbol] = value
        return value


class DefineStatement(Form):

    arity = 3

    def apply(self, environment, *args):
        self.check_arity(args)
        name, arg_names, body = args
        f = UserFunction(name, arg_names, body)
        environment[name] = f
        return name


class UserFunction(Form):

        def __init__(self, name, arg_names, body):
            self.name = name
            self.arity = len(arg_names)
            self.arg_names = list(arg_names)
            self.body = list(body)

        def apply(self, environment, *args):
            self.check_arity(args)
            values = (evaluate(arg, environment) for arg in args)
            local_env = dict(zip(self.arg_names, values))
            invocation_env = collections.ChainMap(local_env, environment)
            return evaluate(self.body, invocation_env)


SPECIAL_FORMS = {
    'if': IfStatement(),
    'set': SetStatement(),
    'begin': BeginStatement(),
    'while': WhileStatement(),
    'define': DefineStatement(),
}

# ______________________________________ Evaluation


global_vars = {}

global_env = collections.ChainMap(global_vars, SPECIAL_FORMS, BUILTINS)


def evaluate(ast, environment):
    if isinstance(ast, int):
        return ast
    elif isinstance(ast, list):
        op = evaluate(ast[0], environment)
        try:
            return op.apply(environment, *ast[1:])
        except ZeroDivisionError as exc:
            raise errors.DivisionByZero from exc

    try:
        return environment[ast]
    except KeyError as exc:
        raise errors.UnknownSymbol(ast) from exc
