todo_list = []

def add_task(task):
    if task:
        todo_list.append(task)
        print("Task Added to the List.\n")
        print("-" * 13)
        view_tasks()
    else:
        print("Invalid Task Input! 😟")

def remove_task(task_num):
    if task_num:
        if task_num > 0 and task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print("Task Removed from the List.\n")
            print("-" * 13)
            view_tasks()
        else:
            print("Invalid Task Number! 😞")

def view_tasks():
    if todo_list:
        print("-" * 13)
        print("Current Tasks:\n")
        for i, task in enumerate(todo_list):
            print(f"{i + 1}. {task}")
        print("-" * 13)
    else:
        print("No Tasks in the List! \nUse Help Menu To Add tasks")

def clear_tasks():
    todo_list.clear()
    print("All Tasks Cleared \n")
    print("-" * 13)

while True:
    print("-" * 13)
    print("\nHelp Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Clear Tasks")
    print("4. View Tasks")
    print("-" * 13)
    choice = input("Enter your choice: \nEg: 1 \n")
    if choice == "1":
        print("-" * 13)
        task = input("Enter the task: \n")
        add_task(task)
    elif choice == "2":
        if todo_list:
            view_tasks()
            task_num = input("Enter the task number to remove: ")
            remove_task(int(task_num))
        else:
            print("No Task Found!\n Use Help Menu To Add tasks")
            print("-" * 13)
    elif choice == "3":
        clear_tasks()
    elif choice == "4":
        view_tasks()
    else:
        print("Invalid Choice! 😞")
        print("-" * 13)