def parse(cmd):
    cmd = cmd.split()
    command = cmd[0]
    arguments = cmd[1:]

    return command, arguments