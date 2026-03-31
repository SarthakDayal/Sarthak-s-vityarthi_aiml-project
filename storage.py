import json
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    for task in tasks:
        if "created_at" not in task:
            task["created_at"] = datetime.now().isoformat()
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)
