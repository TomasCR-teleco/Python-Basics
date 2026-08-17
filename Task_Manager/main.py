#Associate tasks to a category, being able to stablish its state, name, due date and description
########################################################################################################################################
#Analysis:
#   Data input: choice(str), name(category, str), name(task, str), due_date(str), description(str), status(str)
#   Data output: The script doesn't generate any variable to show, it just saves variables and shows them in a certain format.
#   Classes:  1. Task: change state and order the task features.
#             2. Category: save a list of tasks (add, remove), create a list of all pending tasks and order the tasks under its name.
#             3. Manager: save a dictionary of categories, controls task saving, recognises all pending tasks and orders everything.
# Design:
#   1. Ask the user to choose between the menu options:
#   2.1 Add category (1):
#       2.1.1 Ask for the category name.
#       2.1.2 The manager class checks if the category already exists.
#       2.1.3 If it does, it shows an error message and goes back to step 1.
#       2.1.4 If not, it adds the category to the manager dictionary of categories, and goes back to step 1.
#   2.2 Add task (2):
#       2.2.1 Ask for the category name, task title, due date and description (optional).
#       2.2.2 The manager class checks if there are categories.
#       2.2.3 If not, it shows an error message and goes back to step 1.
#       2.2.4 If there are categories, it shows the available ones.
#       2.2.5 Ask the user to choose one, and asks for the task features (title, due date and description).
#       2.2.6 The manager class checks if the category exists.
#       2.2.7 If not, it shows an error message and goes back to step 1.
#       2.2.8 If it does, it adds the task to the category list of tasks, and goes back to step 1.
#   2.3 Show all tasks (3):
#       2.3.1 It checks if the manager class has any category.
#       2.3.2 If not, it chows an error message and goes back to step 1.
#       2.3.3 If there is at least one, it shows all tasks saved in each of the categories own list, and goes back to step 1.
#   2.4 Mark task as completed (4):
#       2.4.1 If checks if the manager class has any category.
#       2.4.2 If not, it shows an error message and goes back to step 1.
#       2.4.3 If there is at least one, it shows all categories, and ask the user to choose one.
#       2.4.4 If the category selected doesn't exist, it shows an error message ang goes back to step 1.
#       2.4.5 If the category selected exists but has no tasks, it shows an error message and goes back to step 1.
#       2.4.6 If the category selected does have tasks, it shows all tasks saved in the category class list.
#       2.4.7 It asks the user to input the number of the task that wants to mark as completed.
#       2.4.8 If there is any ValueError or IndexError, it shows an error message and goes back to step 1.
#       2.4.9 If the input was correct, the chosen task state changes to completed, and goes back to step 1.
#   2.5 Show pending tasks (5):
#       2.5.1 The manager class returns a list with all tasks from the categories that it has saved in its dictionary.
#       2.5.2 If the list is empty (there are no pending tasks), it shows an error message and goes back to step 1.
#       2.5.3 If it isn't it prints all the tasks that the list contains, and goes back to step 1.
#   2.6 Exit (6):
#       2.6.1 Prints "Goodbye!" and exits the program (Doesn't move to step 3)
#   3. Go back to step 1.
################################################################################
from manager import Manager, show_all, show_pending, add_category, add_task, mark_completed
from menu import show_menu
#########################################################################################################################################
def main():
    manager = Manager()
    while True:
        choice = show_menu()
        if choice == "1":
            add_category(manager)
        elif choice == "2":
            add_task(manager)
        elif choice == "3":
            show_all(manager)
        elif choice == "4":
            mark_completed(manager)
        elif choice == "5":
            show_pending(manager)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()