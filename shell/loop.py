def repl():
    try:
        print("$", end=" ")
        cmd = input()
    except EOFError:
        return None

    # check empty input
    if cmd.strip() == "":
            return ""
    return cmd