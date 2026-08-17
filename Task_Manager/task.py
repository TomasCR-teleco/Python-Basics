class Task:
    def __init__(self, title, due_date, description=""):
        self.title = title
        self.due_date = due_date
        self.description = description
        self.completed = False

    def mark_completed(self):
        """Marks the task as completed."""
        self.completed = True

    def mark_incomplete(self):
        """Marks the task as incomplete."""
        self.completed = False

    def __str__(self):
        """Returns a string that represents the task"""
        status = "✓" if self.completed else "✗"
        return f"Task: {self.title}\nDue Date: {self.due_date}\nDescription: {self.description}\nStatus: {status}"