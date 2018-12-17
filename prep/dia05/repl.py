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
        tokens = parser.tokenize(source)
        try:
            ast = parser.parse(tokens)
        except errors.UnexpectedEndOfSource:
            prompt = Prompts.secondary
            continue
        except errors.UnexpectedCloseParen as exc:
            error_msg = str(exc)
        # ______________________________ Evaluate & Print
        if not error_msg:
            try:
                result = evaluator.evaluate(ast)
            except errors.DivisionByZero as exc:
                error_msg = str(exc)
            else:
                print(result)
        if error_msg:
            print('***', error_msg)
            error_msg = ''
        # ______________________________ Loop
        pending_lines = []
        prompt = Prompts.primary


if __name__ == '__main__':
    repl()
