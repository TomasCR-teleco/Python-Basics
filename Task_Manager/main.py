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