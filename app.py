import json
tasks = []


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


def is_valid_task(task):
    return (isinstance(task, dict) and ("title" in task) and ("done" in task) and isinstance(task["title"], str) and isinstance(task["done"], bool))


def get_task_by_index(tasks, index):
    return tasks[index-1]


def is_valid_index(tasks, index):
    return (1 <= index <= len(tasks))


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            loaded_tasks = json.load(file)
            if not isinstance(loaded_tasks, list):
                return []

            valid_tasks = [
                task for task in loaded_tasks if is_valid_task(task)]
            return valid_tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def add_task():
    print(f"Enter your task \n >>>")
    new_task = input()
    if not new_task.strip():
        print("You didnt enter a task, sorry")
    else:
        task = {"title": new_task.strip(), "done": False}
        tasks.append(task)
        save_tasks()


def show_tasks(title):
    if not tasks:
        print("No tasks yet")
    else:
        print(title)
        formatted_list = format_tasks(tasks)
        print("=============================================================")
        for line in formatted_list:
            print(line)
        print("=============================================================")


def format_tasks(tasks):
    return [
        f"{index}.{'[x]' if task['done'] else '[ ]'} {task['title']}" for index, task in enumerate(tasks, start=1)]


def remove_task():
    if not tasks:
        print("No tasks to delete")
        return
    show_tasks("\nYour current list of tasks: \n")
    print("\nEnter task number you want to delete:")

    try:
        task_number = int(input())

        if not is_valid_index(tasks, task_number):
            print("Invalid number")
            return
        tasks.pop(task_number - 1)
        save_tasks()
        show_tasks("\n Task deleted \n Your new list of tasks: \n")
    except ValueError:
        print("\nPlease enter a number \n")


def edit_task():
    if not tasks:
        print("No tasks yet")
        return
    show_tasks("Your current list of tasks")
    print("Enter the number of task u want to change")
    try:
        option = int(input())
        if not is_valid_index(tasks, option):
            print("No task with such number")
            return
        print("Enter a new task name")
        new_task = input()
        task = get_task_by_index(tasks, option)
        task["title"] = new_task.strip()
        save_tasks()
        show_tasks("Your changed list of tasks")
    except ValueError:
        print("Invalid input")


def toggle_task_status():
    if not tasks:
        print("No tasks yet")
        return
    show_tasks("Your current list of tasks")
    print("Enter the number of task u want to change")
    try:
        option = int(input())
        if not is_valid_index(tasks, option):
            print("No task with such number")
            return
        task = get_task_by_index(tasks, option)
        task["done"] = not task["done"]
        save_tasks()
        show_tasks("Your changed list of tasks")
    except ValueError:
        print("Invalid input")


def show_menu():
    while True:
        print("Main Menu")
        print("=============================================================")
        print("1.Add")
        print("2.Show")
        print("3.Remove")
        print("4.Edit task")
        print("5.Mark done")
        print("6.Exit")
        print("=============================================================")
        print("Choose your option(1-6)")
        try:
            option = int(input())
            if option < 1 or option > 6:
                print("Invalid option. Choose between 1 and 6")
                continue
            print("=============================================================")
            if option == 1:
                add_task()
            elif option == 2:
                show_tasks("Your task list:")
            elif option == 3:
                remove_task()
            elif option == 4:
                edit_task()
            elif option == 5:
                toggle_task_status()
            elif option == 6:
                print("GoodBye")
                break
        except ValueError:
            print("\nPlease enter a number(1-6)\n")
            print("=============================================================")


tasks = load_tasks()
show_menu()
