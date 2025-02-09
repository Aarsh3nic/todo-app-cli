

def display():
    file = open("todos.txt", "r")
    arr = file.readlines()
    file.close()
    print("Here's the list:")
    for task in enumerate(arr, start=1):
        print(f" {task[0]}| {task[1].title()}",end="")

def modifyText(arr, message):
    file = open("todos.txt", "w")
    file.writelines(arr)
    file.close()
    print(message)

while True:
    user_action = input("Type add, show, edit or exit:").strip()
    match user_action:
        case "add":
            todo = input("Enter to-do:") + "\n"

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            modifyText(todos,"Added!")

        case "show" | "display":
            display()
        case "edit":
            display()
            num_task = int(input("What task you want to edit (type number): "))
            todos[num_task-1] = input("Enter new task: ") +  "\n"
            modifyText(todos,"Modified!")

        case "complete":
            display()
            num_task = int(input("What task you want to mark as complete (type number): "))
            todos.pop(num_task-1)
            modifyText(todos, "Modified!")
            display()


        case "exit":
            break
        case _:
            print("Invalid Input")


print("Bye")

def display(arr):
    print("Here's the list:")
    for task in enumerate(arr, start=1):
        print(f" {task[0]}| {task[1].title()}")