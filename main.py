

def display():
    taskList = getTaskList()
    print("Here's the list:")
    for task in enumerate(taskList, start=1):
        print(f" {task[0]}| {task[1]}",end="")

def modifyText(arr, message):
    with open("todos.txt", "w") as file:
        file.writelines(arr)
    print(message)

def getTaskList():
    with open("todos.txt", "r") as file:
        taskList = file.readlines()
        return taskList

while True:
    user_action = input("Type add, show, edit or exit:").strip()

    if user_action.startswith("add"):
        todo = user_action[4:].title() + "\n"

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        modifyText(todos,"Added!")

    elif user_action.startswith("show"):
        display()


    elif user_action.startswith("edit"):
        try:
            num_task = int(user_action[5:])
            todos = getTaskList()
            todos[num_task-1] = input("Enter new task: ") +  "\n"
            modifyText(todos,"Modified!")
        except ValueError:
            print("Invalid input, Enter the in format: COMMAND NUMBER\n")
            continue
        except IndexError:
            print(f"No item found at {num_task}.\n")
            continue

    elif user_action.startswith("complete"):
        try:
            num_task = int(user_action[9:])
            todos = getTaskList()
            to_be_removed = todos[num_task-1]
            todos.pop(num_task-1)
            modifyText(todos, f"{to_be_removed[:len(to_be_removed)-1]} removed from the list!")
        except ValueError:
            print("Invalid input, Enter the in format: COMMAND NUMBER\n")
            continue
        except IndexError:
            print(f"No item found at {num_task}.\n")
            continue



    elif user_action.startswith("exit"):
        break

    else: print("Invalid input")


print("Bye")

#new_todos = [item.strip('\n') for item in todos]