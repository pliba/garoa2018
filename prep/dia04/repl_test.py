from pytest import mark

from dialogue.dialogue import Dialogue

from repl import repl


def test_repl_quit(capsys):
    dlg = Dialogue('> .q\n')
    repl(dlg.fake_input)
    captured = capsys.readouterr()
    assert dlg.session == captured.out


@mark.parametrize("session", [
    """
    > (* 111 111)
    12321
    """,
    """
    > (+ 2
    ... 3)
    5
    """,
])
def test_repl(capsys, session):
    dlg = Dialogue(session)
    repl(dlg.fake_input)
    captured = capsys.readouterr()
    assert dlg.session == captured.out


@mark.parametrize("session", [
    """
    > (+ 2
    ... 3)
    5
    > (* 2 3)
    6
    """,

])
def test_repl_multiple_expressions(capsys, session):
    dlg = Dialogue(session)
    repl(dlg.fake_input)
    captured = capsys.readouterr()
    assert dlg.session == captured.out
