def view_task():
    pass


def add_task():
    pass


def remove_task():
    pass


if __name__ == "__main__":
    print("Todo List Menu: ")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")

    ask = int(input("Enter your chocie: "))
    choice = [1, 2, 3]
    if ask not in choice:
        print("Invalid choice!")
