# Introductory Task Manager

## About this project

This project was built as a learning exercise to practice OOP in Python, along with other programming techniques.

## Features

- Create categories to organize tasks.
- Add tasks to a category, with a title, due date, and optional description.
- View all tasks in the system, grouped by category.
- Mark tasks as completed.
- Filter and view only pending tasks.
- Input validation: the program keeps asking until it receives a valid value.

## How to run it

Requires Python 3. From the project folder:

```bash
python main.py
```

## Structure

- `main.py` — entry point of the program: menu, user interaction, and input validation.
- `manager.py` — `Manager` class, which coordinates categories and tasks.
- `category.py` — `Category` class, which groups a list of tasks.
- `task.py` — `Task` class, representing a single task.

## Example

```
--- Task Manager ---
1. Add category
2. Add task
3. Show all tasks
4. Mark task as completed
5. Show pending tasks
6. Exit
Choose an option: 1
Category name: Work

--- Task Manager ---
Choose an option: 2
Available categories: Work
Which category? Work
Task title: Finish project
Due date: 12/09/2024
Description (optional): Complete the final report and submit it.

--- Task Manager ---
Choose an option: 3
Category: Work (1 tasks)
Task: Finish project
Due Date: 12/09/2024
Description: Complete the final report and submit it.
Status: ✗
```