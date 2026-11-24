from task import Task
###########################################################################################################################################
class Category:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        """Adds a task to the class."""
        self.tasks.append(task)

    def remove_task(self, task):
        """Removes a task from the class."""
        if task in self.tasks:
            self.tasks.remove(task)

    def pending_tasks(self):
        """Returns a list with all pending tasks in the category."""
        return [t for t in self.tasks if not t.completed]

    def __str__(self):
        header = f"Category: {self.name} ({len(self.tasks)} tasks)"
        lines = [str(t) for t in self.tasks]
        return header + "\n" + "\n".join(lines)