class UnexpectedEndOfInput(Exception):
    """Unexpected end of input."""


def tokenize(source_code):
    """Converter uma string em uma lista de tokens."""
    return source_code.replace("(", " ( ").replace(")", " ) ").split()


def parse(tokens):
    """Construir expressões aninhadas a partir de uma lista de tokens."""
    try:
        token = tokens.pop(0)
    except IndexError as exc:
        raise UnexpectedEndOfInput() from exc
    try:
        return int(token)  # numeric value
    except ValueError:
        return token  # symbol
