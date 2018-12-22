
def parse(line):
    try:
        return int(line)
    except ValueError:
        return f'<Operator {line}>'
