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
def test_repl_multiple_inputs(capsys, session):
    dlg = Dialogue(session)
    repl(dlg.fake_input)
    captured = capsys.readouterr()
    assert dlg.session == captured.out


@mark.parametrize("session", [
    """
    > (+ 2 3) (* 2 3)
    5
    """,
    """
    > (* 2 3) (
    6
    """,
    """
    > (* 3 4) this will be ignored!
    12
    """,
])
def test_repl_ignore_beyond_first_expression(capsys, session):
    dlg = Dialogue(session)
    repl(dlg.fake_input)
    captured = capsys.readouterr()
    assert dlg.session == captured.out


@mark.parametrize("session", [
    """
    > )
    *** Unexpected close parenthesis.
    """,
    # """
    # > (+ 2 3) )
    # 5 why? should be Unexpected close parenthesis!
    # """,
])
def test_repl_unexpected_close_paren(capsys, session):
    dlg = Dialogue(session)
    repl(dlg.fake_input)
    captured = capsys.readouterr()
    assert dlg.session == captured.out


@mark.parametrize("session", [
    """
    > (/ 1 0)
    *** Division by zero.
    """,
])
def test_repl_error_handling(capsys, session):
    dlg = Dialogue(session)
    repl(dlg.fake_input)
    captured = capsys.readouterr()
    assert dlg.session == captured.out


def test_repl_gcd(capsys):
    session = """
    > (define not (boolval) (if boolval 0 1))
    not
    > (define <> (x y) (not (= x y)))
    <>
    > (define mod (m n) (- m (* n (/ m n))))
    mod
    > (define gcd (m n)
    ...   (begin
    ...       (set r (mod m n))
    ...       (while (<> r 0)
    ...            (begin
    ...                 (set m n)
    ...                 (set n r)
    ...                 (set r (mod m n))))
    ...       n))
    gcd
    > (gcd 6 15)
    3
    """
    dlg = Dialogue(session)
    repl(dlg.fake_input)
    captured = capsys.readouterr()
    assert dlg.session == captured.out
