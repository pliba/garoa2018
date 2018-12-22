import sys

from parser import parse

QUIT_COMMAND = '.q'


def repl(input_fn=input):
    """Read-Eval-Print-Loop"""
    print(f'To exit, type {QUIT_COMMAND}', file=sys.stderr)

    while True:
        try:
            line = input_fn('> ').strip()
        except EOFError:
            break
        if line == QUIT_COMMAND:
            break
        if not line:
            continue

        parsed = parse(line) 
        print(parsed)


if __name__=='__main__':
    repl()
