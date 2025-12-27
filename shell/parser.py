def parse_command(segment):
    tokens = segment.split()

    command = None
    args = []
    stdin = None
    stdout = None
    append = False

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token == ">":
            stdout = tokens[i + 1]
            append = False
            i += 2

        elif token == ">>":
            stdout = tokens[i + 1]
            append = True
            i += 2

        elif token == "<":
            stdin = tokens[i + 1]
            i += 2

        else:
            if command is None:
                command = token
            else:
                args.append(token)
            i += 1

    return {
        "command": command,
        "args": args,
        "stdin": stdin,
        "stdout": stdout,
        "append": append
    }


def parse(command_line):
    # Split pipeline
    segments = [seg.strip() for seg in command_line.split("|")]

    # Single command (no pipe)
    if len(segments) == 1:
        return parse_command(segments[0])

    # Pipeline
    pipeline = []
    for seg in segments:
        pipeline.append(parse_command(seg))

    return pipeline
