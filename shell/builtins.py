from .history import get_all

BUILTINS = ["exit", "echo", "type", "history"]


def is_builtin(command):
    return command in BUILTINS


def execute_builtin(command, args):
    if command == "exit":
        return "exit"

    elif command == "echo":
        print(" ".join(args))
        return True

    elif command == "type":
        if not args:
            return True

        target = args[0]
        if target in BUILTINS:
            print(f"{target} is a shell builtin")
        else:
            print(f"{target}: not found")
        return True

    elif command == "history":
        history = get_all()
        for idx, cmd in enumerate(history, start=1):
            print(f"{idx}  {cmd}")
        return True

    return False
