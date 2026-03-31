from storage import load_tasks, save_tasks

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, title, category="general", priority="medium"):
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "category": category,
            "priority": priority,
            "done": False,
            "done_at": None
        }
        self.tasks.append(task)
        save_tasks(self.tasks)

    def mark_done(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                task["done_at"] = datetime.now().isoformat()
                save_tasks(self.tasks)
                return True
        return False

    def get_tasks(self, category=None, only_pending=False):
        tasks = self.tasks
        if category:
            tasks = [t for t in tasks if t["category"] == category]
        if only_pending:
            tasks = [t for t in tasks if not t["done"]]
        return tasks

    def get_stats(self):
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t["done"])
        pending = total - completed
        categories = set(t["category"] for t in self.tasks)
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "categories": list(categories)
        }
