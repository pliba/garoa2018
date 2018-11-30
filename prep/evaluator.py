import collections
import operator

Operator = collections.namedtuple("Operator", "symbol function")

OPERATORS = [
    Operator("+", operator.add),
    Operator("-", operator.sub),
    Operator("*", operator.mul),
    Operator("/", operator.floordiv),
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
        return BUILTINS[expression]
    elif isinstance(expression, list):  # s-expression
        head = evaluate(expression[0])
        args = (evaluate(e) for e in expression[1:])
        return head.function(*args)
