import textwrap

from pytest import mark

from repl import main


class TextInteraction():

    def __init__(self, session):
        self.session = session
        self.prompts = set()
        self.input_line_gen = iter(self)

    def __iter__(self):
        for line in self.session.splitlines():
            line = line.strip()
            for prompt in self.prompts:
                if line.startswith(prompt):
                    yield line[len(prompt):]
                    break

    def fake_input(self, prompt):
        self.prompts.add(prompt)
        try:
            line = next(self.input_line_gen)
        except StopIteration:
            raise EOFError()
        print(prompt, end='')
        print(line)
        return line

    def __str__(self):
        return textwrap.dedent(self.session.lstrip('\n'))


@mark.parametrize("session", [
    """
    > .q
    """,
    """
    > (* 111 111)
    12321
    """,
    """
    > (* 111
    ... 111)
    12321
    """,
    """
    > (/ 6 0)
    ! Division by zero.
    > (/ 6 3)
    2
    """,
    """
    > (foo 6 0)
    ! Unknown operator: 'foo'.
    """,
    """
    > (9 8 7)
    ! Invalid operator: 9.
    """,
    """
    > (+ 6)
    ! Not enough arguments for operator: '+'.
    > (+ 6 3)
    9
    """,
    """
    > (/ 6 5 4)
    ! Too many arguments for operator: '/'.
    """,
    """
    > )
    ! Unexpected ')'.
    > (+ 2 2)
    4
    """,

])
def test_repl(monkeypatch, capsys, session):
    ti = TextInteraction(session)
    with monkeypatch.context() as m:
        m.setitem(__builtins__, "input", ti.fake_input)
        main()
    captured = capsys.readouterr()
    assert captured.out == str(ti)
