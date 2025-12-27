from .loop import repl
from .parser import parse
from .executor import execute
from .history import add


def main():
    while True:
        cmd_line = repl()

        if cmd_line is None:
            break

        if cmd_line == "":
            continue

        add(cmd_line)

        parsed = parse(cmd_line)
        result = execute(parsed)

        if result == "exit":
            break


if __name__ == "__main__":
    main()
