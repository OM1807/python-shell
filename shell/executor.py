import subprocess
import sys

from builtins import is_builtin, execute_builtin
from path import find_executable


def execute(parsed):
    if isinstance(parsed, list):
        return execute_pipeline(parsed)
    return execute_single(parsed)


def execute_single(parsed):
    command = parsed["command"]
    args = parsed["args"]
    stdin_file = parsed["stdin"]
    stdout_file = parsed["stdout"]
    append = parsed["append"]

    original_stdin = sys.stdin
    original_stdout = sys.stdout

    input_handle = None
    output_handle = None

    try:
        if stdin_file:
            input_handle = open(stdin_file, "r")
            sys.stdin = input_handle

        if stdout_file:
            mode = "a" if append else "w"
            output_handle = open(stdout_file, mode)
            sys.stdout = output_handle

        if is_builtin(command):
            return execute_builtin(command, args)

        executable = find_executable(command)
        if executable is None:
            print(f"{command}: command not found")
            return None

        subprocess.run(
            [executable] + args,
            stdin=sys.stdin,
            stdout=sys.stdout
        )

    finally:
        if input_handle:
            input_handle.close()
        if output_handle:
            output_handle.close()

        sys.stdin = original_stdin
        sys.stdout = original_stdout


def execute_pipeline(pipeline):
    processes = []
    prev_pipe = None

    for i, cmd in enumerate(pipeline):
        command = cmd["command"]
        args = cmd["args"]

        if is_builtin(command):
            print(f"{command}: cannot be used in pipeline")
            return None

        executable = find_executable(command)
        if executable is None:
            print(f"{command}: command not found")
            return None

        if i < len(pipeline) - 1:
            proc = subprocess.Popen(
                [executable] + args,
                stdin=prev_pipe,
                stdout=subprocess.PIPE
            )
        else:
            proc = subprocess.Popen(
                [executable] + args,
                stdin=prev_pipe
            )

        if prev_pipe:
            prev_pipe.close()

        prev_pipe = proc.stdout
        processes.append(proc)

    for proc in processes:
        proc.wait()
