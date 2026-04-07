import json
tasks = []


def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except:
        FileNotFoundError
    pass


def add_task():
    print(f"Enter your task \n >>>")
    new_task = input()
    if not new_task.strip():
        print("You didnt enter a task, sorry")
    else:
        tasks.append(new_task.strip())
        save_tasks()


def show_tasks(title):
    if not tasks:
        print("No tasks yet")
    else:
        print(title)
        print("=============================================================")
        for index, task in enumerate(tasks, start=1):
            print(index, task)
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


load_tasks()
show_menu()
