def repl():
    try:
        print("$", end=" ")
        cmd = input()
    except EOFError:
        return None

    if cmd.strip() == "":
        return ""

    return cmd
