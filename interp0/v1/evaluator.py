import collections
import operator


class EvaluationError(Exception):
    """Error while evaluating expression."""

    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        msg = self.__class__.__doc__
        if self.value is not None:
            msg = msg.rstrip(".")
            msg += ": " + repr(self.value) + "."
        return msg


class InvalidExpression(EvaluationError):
    """Invalid expression."""


class InvalidOperator(EvaluationError):
    """Invalid operator."""


class MissingArgument(EvaluationError):
    """Not enough arguments for operator."""


class TooManyArguments(EvaluationError):
    """Too many arguments for operator."""


class UnknownOperator(EvaluationError):
    """Unknown operator."""


class EmptyExpression(EvaluationError):
    """Empty expression."""


Operator = collections.namedtuple("Operator", "symbol function arity")

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
            raise UnknownOperator(expression) from exc

    elif isinstance(expression, list):  # s-expression
        if len(expression) == 0:
            raise EmptyExpression()
        head = evaluate(expression[0])
        if isinstance(head, Operator):
            args = expression[1:]
            if len(args) < head.arity:
                raise MissingArgument(head.symbol)
            elif len(args) > head.arity:
                raise TooManyArguments(head.symbol)
            values = [evaluate(e) for e in args]
            return head.function(*values)
        else:
            raise InvalidOperator(expression[0])

    else:
        raise InvalidExpression()
