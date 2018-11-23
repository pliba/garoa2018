import operator
import errors


class Operator:

    def __init__(self, symbol, function, arity):
        self.symbol = symbol
        self.function = function
        self.arity = arity

    def __eq__(self, other):
        return all([
            self.symbol == other.symbol,
            self.function == other.function,
            self.arity == other.arity,
        ])

    def evaluate(self, arg_list):
        if len(arg_list) < self.arity:
            raise errors.MissingArgument(self.symbol)
        elif len(arg_list) > self.arity:
            raise errors.TooManyArguments(self.symbol)
        values = [evaluate(e) for e in arg_list]
        return self.function(*values)


OPERATORS = [
    Operator("+", operator.add, 2),
    Operator("-", operator.sub, 2),
    Operator("*", operator.mul, 2),
    Operator("/", operator.floordiv, 2),
]

BUILTINS = {op.symbol: op for op in OPERATORS}


def evaluate(expression):
    """Computar o valor da expression.

    Expression é um AST: valores simples ou listas aninhadas
    representando uma expressão.
    """
    if isinstance(expression, int):  # valor numérico
        return expression

    elif isinstance(expression, str):  # símbolo
        try:
            return BUILTINS[expression]
        except KeyError as exc:
            raise errors.UnknownOperator(expression) from exc

    elif isinstance(expression, list):  # s-expression
        if len(expression) == 0:
            raise errors.EmptyExpression()
        head = evaluate(expression[0])
        try:
            return head.evaluate(expression[1:])
        except AttributeError as exc:
            raise errors.InvalidOperator(expression[0]) from exc

    else:
        raise errors.InvalidExpression()
