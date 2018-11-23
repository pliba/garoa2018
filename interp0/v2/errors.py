class InterpreterError(Exception):
    """Error while evaluating expression."""

    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        msg = self.__class__.__doc__
        if self.value is not None:
            msg = msg.rstrip(".")
            msg += ": " + repr(self.value) + "."
        return msg


class ParsingError(Exception):
    """Generic error while parsing source code."""

    def __str__(self):
        return self.__class__.__doc__


class UnexpectedEndOfSource(InterpreterError):
    """Unexpected end of source code."""


class UnexpectedCloseParen(InterpreterError):
    """Unexpected ')'."""


class InvalidExpression(InterpreterError):
    """Invalid expression."""


class InvalidOperator(InterpreterError):
    """Invalid operator."""


class MissingArgument(InterpreterError):
    """Not enough arguments for operator."""


class TooManyArguments(InterpreterError):
    """Too many arguments for operator."""


class UnknownOperator(InterpreterError):
    """Unknown operator."""


class EmptyExpression(InterpreterError):
    """Empty expression."""
