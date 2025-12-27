import os


def find_executable(command):
    if "/" in command:
        if os.path.isfile(command) and os.access(command, os.X_OK):
            return command
        return None

    path_env = os.environ.get("PATH")
    if not path_env:
        return None

    for directory in path_env.split(":"):
        full_path = os.path.join(directory, command)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path

    return None
