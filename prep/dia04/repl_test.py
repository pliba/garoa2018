from pytest import mark

from dialogue import Dialogue

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
])
def test_repl(capsys, session):
    dlg = Dialogue(session)
    repl(dlg.fake_input)
    captured = capsys.readouterr()
    assert dlg.session == captured.out
