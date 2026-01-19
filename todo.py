# To-Do List Application
# Software Engineering (SEN) Project

tasks = []

def add_task():
    task_name = input("Enter task description: ")
    task = {
        "name": task_name,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!\n")

def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return

    print("\nTo-Do List:")
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['name']} - {status}")
    print()

def complete_task():
    view_tasks()
    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to mark as completed: "))
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed!\n")
    except (ValueError, IndexError):
        print("Invalid task number.\n")

def delete_task():
    view_tasks()
    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to delete: "))
        deleted_task = tasks.pop(task_number - 1)
        print(f"Task '{deleted_task['name']}' deleted successfully!\n")
    except (ValueError, IndexError):
        print("Invalid task number.\n")

def menu():
    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

menu()