

def display():
    with open("todos.txt", "r") as file:
        arr = file.readlines()

    print("Here's the list:")
    for task in enumerate(arr, start=1):
        print(f" {task[0]}| {task[1]}",end="")
    return arr

def modifyText(arr, message):
    with open("todos.txt", "w") as file:
        file.writelines(arr)
    print(message)

while True:
    user_action = input("Type add, show, edit or exit:").strip()

    if "add" in user_action[0:3]:
        todo = user_action[4:].title() + "\n"

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        modifyText(todos,"Added!")

    elif "show" in user_action[0:7]:
        display()

    elif "edit" in user_action[0:4]:
        display()
        num_task = int(user_action[5:])
        todos[num_task-1] = input("Enter new task: ") +  "\n"
        modifyText(todos,"Modified!")

    elif "complete" in user_action[0:8]:

        num_task = int(user_action[9:])
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        to_be_removed = todos[num_task-1]
        todos.pop(num_task-1)
        modifyText(todos, f"{to_be_removed[:len(to_be_removed)-1]} removed from the list!")
        #display()


    elif "exit" in user_action[0:4]:
        break

    else: print("Invalid input")


print("Bye")

#new_todos = [item.strip('\n') for item in todos]