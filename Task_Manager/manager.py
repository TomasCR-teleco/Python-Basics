from task import Task
from category import Category
from validation import ask_text
##########################################################################################################################################
class Manager:
    def __init__(self):
        self.categories = {}

    def add_category(self, name):
        """Adds a new category to the manager."""
        if name in self.categories:
            print(f"Category '{name}' already exists.")
            return
        self.categories[name] = Category(name)

    def add_task(self, category_name, task):
        """Adds a task to a specific category"""
        if category_name not in self.categories:
            print(f"Category '{category_name}' doesn't exist.")
            return
        self.categories[category_name].add_task(task)

    def all_pending_tasks(self):
        """Returns a list of all pending tasks in all categories."""
        pending = []
        for category in self.categories.values():
            pending.extend(category.pending_tasks())
        return pending

    def __str__(self):
        if not self.categories:
            return "No categories yet."
        return "\n\n".join(str(cat) for cat in self.categories.values())

def show_all(manager):
    print(manager)

def show_pending(manager):
    pending = manager.all_pending_tasks()
    if not pending:
        print("No pending tasks.")
        return
    for task in pending:
        print(task)
        print()

def add_category(manager):
    name = ask_text("Category name: ")
    manager.add_category(name)

def add_task(manager):
    if not manager.categories:
        print("No categories yet. Create one first.")
        return
    print("Available categories:", ", ".join(manager.categories.keys()))
    category_name = ask_text("Which category? ")
    title = ask_text("Task title: ")
    due_date = ask_text("Due date: ")
    description = ask_text("Description (optional): ")
    task = Task(title, due_date, description)
    manager.add_task(category_name, task)

def mark_completed(manager):
    if not manager.categories:
        print("No categories yet.")
        return
    print("Available categories:", ", ".join(manager.categories.keys()))
    category_name = ask_text("Which category? ")
    if category_name not in manager.categories:
        print("That category doesn't exist.")
        return
    
    category = manager.categories[category_name]
    if not category.tasks:
        print("This category has no tasks.")
        return
    
    for i, task in enumerate(category.tasks):
        print(f"{i}. {task.title}")
    try:
        index = int(ask_text("Which task number? "))
        category.tasks[index].mark_completed()
        print("Marked as completed.")
    except (ValueError, IndexError):
        print("Invalid task number.")