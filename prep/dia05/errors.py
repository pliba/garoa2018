class InterpreterException(Exception):
    """Generic interpreter exception."""


class UnexpectedEndOfSource(InterpreterException):
    """Unexpected end of source code."""


class UnexpectedCloseParen(InterpreterException):
    """Unexpected close parenthesis."""


class EvaluatorException(InterpreterException):
    """Generic evaluator exception."""


class MissingArgument(EvaluatorException):
    """Missing argument."""


class TooManyArguments(EvaluatorException):
    """Too many arguments."""


class DivisionByZero(EvaluatorException):
    """Division by zero."""
