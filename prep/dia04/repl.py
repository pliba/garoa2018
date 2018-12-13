#!/usr/bin/env python3

import sys

QUIT_COMMAND = '.q'


class Prompts:
    primary = '>'
    secondary = '...'


def repl(input_fn=input):
    prompt = Prompts.primary
    print(f'To exit, type {QUIT_COMMAND}', file=sys.stderr)
    while True:
        # ______________________________ Read
        current = input_fn(prompt + ' ').strip(' ')
        if current == QUIT_COMMAND:
            break


if __name__ == '__main__':
    repl()
