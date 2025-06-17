tasks = []

def show_menu():
    print("\nTo-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "✓" if task['done'] else "✗"
            print(f"{idx}. [{status}] {task['task']}")

def add_task():
    task = input("Enter the task: ")
    tasks.append({'task': task, 'done': False})
    print("Task added.")

def mark_done():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: "))
        tasks[task_num - 1]['done'] = True
        print("Task marked as done.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_num - 1)
        print(f"Removed task: {removed['task']}")
    except (IndexError, ValueError):
        print("Invalid task number.")
        
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Exiting the To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
