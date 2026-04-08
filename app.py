import json
tasks = []


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except:
        FileNotFoundError


def add_task():
    print(f"Enter your task \n >>>")
    new_task = input()
    if not new_task.strip():
        print("You didnt enter a task, sorry")
    else:
        task_dict = {"title": new_task, "done": False}
        tasks.append(task_dict)
        save_tasks()


def show_tasks(title):
    if not tasks:
        print("No tasks yet")
    else:
        print(title)
        print("=============================================================")
        for task in tasks:
            print(task["title"], task["done"])
        print("=============================================================")


def remove_task():
    if not tasks:
        print("No tasks to delete")
        return
    show_tasks("\nYour current list of tasks: \n")
    print("\nEnter task number you want to delete:")

    try:
        task_number = int(input())

        if task_number < 1 or task_number > len(tasks):
            print("Invalid number")
            return
        tasks.pop(task_number - 1)
        save_tasks()
        show_tasks("\n Task deleted \n Your new list of tasks: \n")
    except ValueError:
        print("\nPlease enter a number \n")


def show_menu():
    while True:
        print("Main Menu")
        print("=============================================================")
        print("1.Add")
        print("2.Show")
        print("3.Remove")
        print("4.Exit")
        print("=============================================================")
        print("Choose your option(1-4)")
        try:
            option = int(input())
            if option < 1 or option > 4:
                print("Invalid option. Choose between 1 and 4")
                continue
            print("=============================================================")
            if option == 1:
                add_task()
            elif option == 2:
                show_tasks("Your task list:")
            elif option == 3:
                remove_task()
            elif option == 4:
                print("GoodBye")
                break
        except ValueError:
            print("\nPlease enter a number(1-4)\n")
            print("=============================================================")


tasks = load_tasks()
show_menu()
