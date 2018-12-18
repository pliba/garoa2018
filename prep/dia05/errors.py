class InterpreterException(Exception):
    """Generic interpreter exception."""

    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        msg = self.__class__.__doc__
        if self.value is not None:
            msg = msg.rstrip(".")
            msg += ": " + repr(self.value) + "."
        return msg

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

class UnknownSymbol(EvaluatorException):
    """Unknown symbol."""
