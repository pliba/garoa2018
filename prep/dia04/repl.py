#!/usr/bin/env python3

import sys

import parser
import evaluator


QUIT_COMMAND = '.q'


class Prompts:
    primary = '>'
    secondary = '...'


def repl(input_fn=input):
    prompt = Prompts.primary
    print(f'To exit, type {QUIT_COMMAND}', file=sys.stderr)
    while True:
        # ______________________________ Read
        try:
            source = input_fn(prompt + ' ').strip(' ')
        except EOFError:
            break
        if source == QUIT_COMMAND:
            break
        # ______________________________ Parse
        expr = parser.parse(parser.tokenize(source))
        # ______________________________ Evaluate & Print
        result = evaluator.evaluate(expr)
        print(result)


if __name__ == '__main__':
    repl()
