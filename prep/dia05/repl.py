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
    error_msg = ''
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
        except errors.UnexpectedCloseParen:
            error_msg = '*** Unexpected close parenthesis.'
        # ______________________________ Evaluate & Print
        if not error_msg:
            result = evaluator.evaluate(ast)
            print(result)
        else:
            print(error_msg)
            error_mst = ''
        # ______________________________ Loop
        pending_lines = []
        prompt = Prompts.primary


if __name__ == '__main__':
    repl()
