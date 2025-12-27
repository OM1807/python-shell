🐚 Advanced Unix-like Shell in Python

An advanced Unix-like shell implemented in Python, supporting core shell features such as command parsing, built-in commands, PATH-based execution, input/output redirection, pipelines, and command history.
This project demonstrates operating-system concepts, process management, and clean modular design.

✨ Features
1. Core Shell Capabilities

Interactive REPL (Read–Eval–Print Loop)

Graceful exit using Ctrl+D

Robust command parsing

Modular architecture with clear separation of concerns

2. Built-in Commands

exit – Exit the shell

echo – Print arguments to standard output

type – Identify whether a command is a shell builtin

history – Display previously executed commands

3. External Command Execution

PATH-based executable lookup

Executes system commands (ls, pwd, whoami, etc.)

Proper process handling using subprocess

4. Advanced Unix Features

Input redirection (<)

Output redirection (>)

Append redirection (>>)

Pipelines (|) with multi-process execution

Correct stdin/stdout restoration after execution

5. Command History

Stores all user-entered commands (except empty input)

history builtin displays numbered command list

🧠 Architecture Overview

The shell is designed in a layered and modular way, similar to real Unix shells.

User
 ↓
REPL (loop.py)
 ↓
History Manager (history.py)
 ↓
Parser (parser.py)
 ↓
Executor (executor.py)
 ├── Builtins (builtins.py)
 └── PATH Resolver (path.py)
 ↓
Operating System

File Responsibilities
File	Responsibility
loop.py	Reads user input (REPL)
main.py	Controls shell lifecycle and orchestration
parser.py	Parses commands, redirection, and pipelines
executor.py	Executes builtins, external commands, pipes
builtins.py	Shell built-in command implementations
path.py	PATH-based executable resolution
history.py	Command history storage and retrieval
📂 Project Structure
python_shell/
└── shell/
    ├── __init__.py
    ├── main.py
    ├── loop.py
    ├── parser.py
    ├── executor.py
    ├── builtins.py
    ├── path.py
    └── history.py

▶️ How to Run

From the project root directory:

python -m shell.main


You will see a shell prompt:

$

🧪 Example Usage
$ ls -l
$ echo hello world
$ echo hello > out.txt
$ cat < out.txt
$ ls | wc -l
$ history
1  ls -l
2  echo hello world
3  echo hello > out.txt
4  cat < out.txt
5  ls | wc -l
6  history
$ exit

🚀 Skills & Concepts Demonstrated

Unix shell design principles

Process creation and management

Inter-process communication using pipes

File descriptor redirection

Modular Python architecture

Systems programming concepts

Error handling and resource cleanup


📜 License

This project is for educational and learning purposes.