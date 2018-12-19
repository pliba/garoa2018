import textwrap


class Dialogue():
    """ ``Dialogue`` allows testing of text-based interactions or REPLs.

        A ``Dialogue`` instance is created with a session argument: a
        multi-line string with prompts, user inputs and expected outputs.
        Each time the ``fake_input`` method is called, it emulates the
        Python 3 ``input`` built-in function by printing a prompt, then
        a user input, and returning that input. Therefore, ``fake_input``
        can be used to mock ``input``, providing pre-recorded "user"
        inputs to the REPL under test.
    """

    def __init__(self, session):
        # dedent session given as indented string (see tests)
        self.session = textwrap.dedent(session.lstrip('\n'))
        self.input_line_gen = iter(self)
        self.prompt = ''

    def __iter__(self):
        for line in self.session.splitlines():
            if line.startswith(self.prompt):
                yield line[len(self.prompt):]

    def fake_input(self, prompt):
        """Use this method to mock the ``input`` built-in."""
        self.prompt = prompt
        try:
            line = next(self.input_line_gen)
        except StopIteration:
            raise EOFError()
        print(prompt + line)
        return line
