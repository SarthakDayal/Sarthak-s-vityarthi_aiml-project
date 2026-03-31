from task_manager import TaskManager

def show_menu():
    print("\nSmart Task Manager")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Mark task as done")
    print("4. Show stats")
    print("5. Exit")

def main():
    tm = TaskManager()
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            title = input("Task title: ")
            category = input("Category (default 'general'): ") or "general"
            priority = input("Priority (low/medium/high): ") or "medium"
            tm.add_task(title, category, priority)
            print("Task added!")
        elif choice == "2":
            category = input("Filter by category (or leave empty): ")
            only_pending = input("Show only pending? (y/n): ").lower() == "y"
            tasks = tm.get_tasks(category=category or None, only_pending=only_pending)
            for t in tasks:
                status = "✅ Done" if t["done"] else "⏳ Pending"
                print(f"{t['id']}. {t['title']} [{t['category']}, {t['priority']}] {status}")
        elif choice == "3":
            task_id = int(input("Task ID to mark done: "))
            if tm.mark_done(task_id):
                print("Task marked done.")
            else:
                print("Task not found.")
        elif choice == "4":
            stats = tm.get_stats()
            print(f"Total: {stats['total']}, Completed: {stats['completed']}, Pending: {stats['pending']}")
            print(f"Categories: {stats['categories']}")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
