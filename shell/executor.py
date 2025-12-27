import subprocess
import sys

from builtins import is_builtin, execute_builtin
from path import find_executable


def execute(parsed):
    command = parsed["command"]
    args = parsed["args"]
    stdin_file = parsed["stdin"]
    stdout_file = parsed["stdout"]
    append = parsed["append"]

    # Save original streams
    original_stdin = sys.stdin
    original_stdout = sys.stdout

    input_handle = None
    output_handle = None

    try:
        # Handle input redirection
        if stdin_file:
            input_handle = open(stdin_file, "r")
            sys.stdin = input_handle

        # Handle output redirection
        if stdout_file:
            mode = "a" if append else "w"
            output_handle = open(stdout_file, mode)
            sys.stdout = output_handle

        # Built-in commands
        if is_builtin(command):
            result = execute_builtin(command, args)
            return result

        # External command
        executable = find_executable(command)
        if executable is None:
            print(f"{command}: command not found")
            return None

        subprocess.run(
            [executable] + args,
            stdin=sys.stdin,
            stdout=sys.stdout
        )

    except FileNotFoundError as e:
        print(f"file error: {e}")

    except PermissionError:
        print(f"{command}: permission denied")

    finally:
        # Restore original streams
        if input_handle:
            input_handle.close()
        if output_handle:
            output_handle.close()

        sys.stdin = original_stdin
        sys.stdout = original_stdout
