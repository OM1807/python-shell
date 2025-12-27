# 🐚 Advanced Unix-Like Shell in Python

A fully functional **advanced Unix-like shell** implemented in Python.  
This project demonstrates **systems programming concepts**, **process management**, and **clean modular design**, inspired by real Unix shells such as `bash`.

---

## 📌 Overview

This shell supports:

- Interactive command execution (REPL)
- Built-in commands
- PATH-based external command execution
- Input / Output redirection
- Command pipelines
- Command history

The project is designed incrementally and cleanly, making it **resume-ready** and **interview-friendly**.

---

## ✨ Features

### 🟢 Core Shell
- Interactive REPL (`$` prompt)
- Graceful exit using `Ctrl+D`
- Modular architecture
- Clean separation of concerns

### 🟢 Built-in Commands
| Command | Description |
|------|-----------|
| `exit` | Exit the shell |
| `echo` | Print arguments |
| `type` | Identify builtin commands |
| `history` | Show command history |

### 🟢 External Commands
- PATH-based executable resolution
- Runs system commands (`ls`, `pwd`, `whoami`, etc.)
- Uses `subprocess` for safe execution

### 🟢 Advanced Unix Features
- Input redirection `<`
- Output redirection `>`
- Append redirection `>>`
- Pipelines `|`
- Multi-process execution with OS pipes
- Proper stdin/stdout restoration

### 🟢 Command History
- Stores all user-entered commands
- `history` builtin prints numbered list
- Includes successful and failed commands

---

## 🧠 Architecture

The shell is structured similarly to real Unix shells.

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

---

## 🧩 Module Responsibilities

| File | Responsibility |
|----|---------------|
| `loop.py` | Read user input (REPL) |
| `main.py` | Shell lifecycle & orchestration |
| `parser.py` | Parse commands, redirection & pipes |
| `executor.py` | Execute builtins, pipelines & programs |
| `builtins.py` | Built-in shell commands |
| `path.py` | PATH-based executable lookup |
| `history.py` | Command history management |

---

## 📂 Project Structure

python_shell/
└── shell/
├── init.py
├── main.py
├── loop.py
├── parser.py
├── executor.py
├── builtins.py
├── path.py
└── history.py

---

## ▶️ How to Run

From the **project root directory**:

```bash
python -m shell.main

You will see:
$

Now you can start the shell 