# Sarthak-s-vityarthi_aiml-project
# Smart Task Manager with Priority & Analytics

A simple Python‑based command‑line task manager that helps you add, organize, and track tasks with priorities and basic analytics. Perfect for students who want to practice data structures and file handling in Python.

## Features

- Add tasks with title, category, and priority.
- Mark tasks as done and track completion over time.
- View tasks filtered by category and pending/completed status.
- View simple statistics (total, completed, pending, categories).

## How to run

### Prerequisites

- Python 3.7 or higher installed on your machine.
```bash
python --version
```


### 1. Clone the repository

```bash
git clone https://github.com/your-username/smart-task-manager.git
cd smart-task-manager
```

### 2. Install dependencies (optional, currently none)

There are no external libraries; the project runs with the Python standard library.

### 3. Run the application

```bash
python main.py
```

Follow the on‑screen menu to:
- Add tasks.
- View tasks (optionally filtered by category or pending/completed).
- Mark tasks as done.
- View simple statistics about your tasks.

## Project structure

- `main.py` – main command‑line interface.
- `task_manager.py` – core `TaskManager` class with all business logic.
- `storage.py` – functions to load and save tasks to `tasks.json`.
- `requirements.txt` – project dependencies (currently empty).
- `sample_report_draft.md` – draft content for your project report (you can adapt this).

## Course relevance

This project demonstrates:
- Use of **data structures** (lists, dictionaries) to represent tasks.
- Basic **algorithms** for filtering, counting, and searching.
- **File handling** with JSON for persistence.
- Modular Python code organization and readability.

## Future improvements

- Add a simple GUI using `tkinter` or a web interface with `Flask`.
- Implement a priority queue for sorting tasks by priority.
- Add due dates and reminders.

---

## 📝 License

This project is for educational use only. You are free to adapt and extend it for your coursework.
