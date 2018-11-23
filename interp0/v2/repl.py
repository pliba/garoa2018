import sys

import parser
import evaluator
import errors

QUIT_COMMAND = '.q'


def main():
    prompt = '>'
    pending_lines = []
    print(f'To exit, type: {QUIT_COMMAND}', file=sys.stderr)
    while True:
        # ______________________________ Read
        try:
            current = input(prompt + ' ').strip(' ')
        except EOFError:
            break
        if current == QUIT_COMMAND:
            break
        if current == '':
            prompt = '...'
            continue
        pending_lines.append(current)
        # ______________________________ Parse
        source = ' '.join(pending_lines)
        expr = None
        try:
            expr = parser.parse(parser.tokenize(source))
        except errors.UnexpectedEndOfSource:
            prompt = '...'
            continue
        except errors.UnexpectedCloseParen as exc:
            print(f'! {exc}')
        # ______________________________ Evaluate & Print
        if expr is not None:
            try:
                result = evaluator.evaluate(expr)
            except ZeroDivisionError:
                print('! Division by zero.')
            except (errors.UnknownOperator, errors.InvalidOperator,
                    errors.MissingArgument, errors.TooManyArguments,
                    ) as exc:
                print(f'! {exc}')
            else:
                print(result)
        prompt = '>'
        pending_lines = []
        # ______________________________ Loop


if __name__ == '__main__':
    main()
