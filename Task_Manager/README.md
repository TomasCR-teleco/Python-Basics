# Introductory Task Manager

> Associate tasks to a category, being able to establish its state, name, due date and description.

---

## 📝 About this project

This project was built as a learning exercise to practice OOP in Python, along with other programming techniques.

---

## ✨ Features

- Create categories to organize tasks.
- Add tasks to a category, with a title, due date, and optional description.
- View all tasks in the system, grouped by category.
- Mark tasks as completed.
- Filter and view only pending tasks.
- Input validation: the program keeps asking until it receives a valid value.

---

## 🏗️ Technical Analysis

### Data Specifications

| Data Type | Attributes / Variables | Description |
| :--- | :--- | :--- |
| **Input Data** | `choice` (str), `category_name` (str), `task_name` (str), `due_date` (str), `description` (str), `status` (str) | Raw inputs collected via CLI user prompts |
| **Output Data** | Console UI Render | The script doesn't generate any variable to show, it just saves variables and shows them in a certain format |

### Core Classes

- **`Task`** (`task.py`): Change state and order the task features.
- **`Category`** (`category.py`): Save a list of tasks (add, remove), create a list of all pending tasks and order the tasks under its name.
- **`Manager`** (`manager.py`): Save a dictionary of categories, controls task saving, recognises all pending tasks and orders everything.

---

## ⚙️ Design & Workflow

### Menu Operations

#### 1. Add Category
1. Ask for the category name.
2. The `Manager` class checks if the category already exists.
   - **Exists:** Shows an error message $\rightarrow$ Goes back to step 1.
   - **Does not exist:** Adds the category to the `Manager` dictionary of categories $\rightarrow$ Goes back to step 1.

#### 2. Add Task
1. The `Manager` class checks if there are categories.
   - **No categories:** Shows an error message $\rightarrow$ Goes back to step 1.
   - **Categories exist:** Shows the available ones.
2. Ask the user to choose one, and ask for the task features (title, due date and description — optional).
3. The `Manager` class checks if the category exists.
   - **Does not exist:** Shows an error message $\rightarrow$ Goes back to step 1.
   - **Exists:** Adds the task to the category list of tasks $\rightarrow$ Goes back to step 1.

#### 3. Show All Tasks
1. Checks if the `Manager` class has any category.
   - **No categories:** Shows an error message $\rightarrow$ Goes back to step 1.
   - **At least one category:** Shows all tasks saved in each of the categories own list $\rightarrow$ Goes back to step 1.

#### 4. Mark Task as Completed
1. Checks if the `Manager` class has any category.
   - **No categories:** Shows an error message $\rightarrow$ Goes back to step 1.
   - **At least one category:** Shows all categories, and asks the user to choose one.
2. Check selected category:
   - **Category doesn't exist:** Shows an error message $\rightarrow$ Goes back to step 1.
   - **Category exists but has no tasks:** Shows an error message $\rightarrow$ Goes back to step 1.
   - **Category has tasks:** Shows all tasks saved in the category class list.
3. Ask the user to input the number of the task that wants to mark as completed.
   - **`ValueError` or `IndexError`:** Shows an error message $\rightarrow$ Goes back to step 1.
   - **Correct input:** The chosen task state changes to completed $\rightarrow$ Goes back to step 1.

#### 5. Show Pending Tasks
1. The `Manager` class returns a list with all tasks from the categories that it has saved in its dictionary.
2. Check returned list:
   - **Empty list:** Shows an error message $\rightarrow$ Goes back to step 1.
   - **Not empty:** Prints all the tasks that the list contains $\rightarrow$ Goes back to step 1.

#### 6. Exit
1. Prints `"Goodbye!"` and exits the program (doesn't move to step 3).

---

## 📁 File Structure

- `main.py` — Entry point of the program: menu, user interaction, and input validation.
- `manager.py` — `Manager` class, which coordinates categories and tasks.
- `category.py` — `Category` class, which groups a list of tasks.
- `task.py` — `Task` class, representing a single task.

---

## 🚀 How to run it

Requires Python 3. From the project folder:

```bash
python main.py
```