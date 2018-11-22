class InterpreterError(Exception):
    """Generic interpreter error."""

    def __str__(self):
        return self.__class__.__doc__


class UnexpectedEndOfInput(InterpreterError):
    """Unexpected end of input."""


class UnexpectedCloseParen(InterpreterError):
    """Unexpected ')'."""


def tokenize(source_code):
    """Converter uma string em uma lista de tokens."""
    return source_code.replace("(", " ( ").replace(")", " ) ").split()


def parse(tokens):
    """Construir expressões aninhadas a partir de uma lista de tokens."""
    try:
        token = tokens.pop(0)
    except IndexError as exc:
        raise UnexpectedEndOfInput() from exc
    if token == "(":  # s-expression
        ast = []
        while tokens and tokens[0] != ")":
            ast.append(parse(tokens))
        if not tokens:
            raise UnexpectedEndOfInput()
        tokens.pop(0)  # drop ')'
        return ast
    elif token == ")":
        raise UnexpectedCloseParen()
    try:
        return int(token)  # valor numérico
    except ValueError:
        return token  # símbolo
