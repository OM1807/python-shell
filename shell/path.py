import os


def find_executable(command):
    
    # Finds the full path of an executable using PATH.

    # If command contains a slash, treat it as a path
    if "/" in command:
        if os.path.isfile(command) and os.access(command, os.X_OK):
            return command
        return None

    # Get PATH environment variable
    path_env = os.environ.get("PATH")
    if not path_env:
        return None

    # Split PATH into directories
    paths = path_env.split(":")

    # Search for executable in PATH directories
    for directory in paths:
        full_path = os.path.join(directory, command)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path

    return None
