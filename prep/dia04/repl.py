#!/usr/bin/env python3

import sys

import parser
import evaluator
import errors

QUIT_COMMAND = '.q'


class Prompts:
    primary = '>'
    secondary = '...'


def repl(input_fn=input):
    prompt = Prompts.primary
    pending_lines = []
    print(f'To exit, type {QUIT_COMMAND}', file=sys.stderr)
    while True:
        # ______________________________ Read
        try:
            current = input_fn(prompt + ' ').strip(' ')
        except EOFError:
            break
        if current == QUIT_COMMAND:
            break
        pending_lines.append(current)
        # ______________________________ Parse
        source = ' '.join(pending_lines)
        try:
            ast = parser.parse(parser.tokenize(source))
        except errors.UnexpectedEndOfSource:
            prompt = Prompts.secondary
            continue
        # ______________________________ Evaluate & Print
        result = evaluator.evaluate(ast)
        print(result)
        # ______________________________ Loop
        pending_lines = []
        prompt = Prompts.primary


if __name__ == '__main__':
    repl()
