todos = []

def display(arr):
    print("Here's the list:")
    for task in enumerate(arr, start=1):
        print(f" {task[0]}| {task[1].title()}")

while True:
    user_action = input("Type add, show, edit or exit:").strip()
    match user_action:
        case "add":
            todo = input("Enter to-do:")
            todos.append(todo)
        case "show" | "display":
            display(todos)
        case "edit":
            display(todos)
            num_task = int(input("What task you want to edit (type number): "))
            todos[num_task-1] = input("Enter new task: ")
            print("Modified!")

        case "complete":
            display(todos)
            num_task = int(input("What task you want to mark as complete (type number): "))
            todos.pop(num_task-1)
            print("Modified!")
            display(todos)


        case "exit":
            break
        case _:
            print("Invalid Input")


print("Bye")

def display(arr):
    print("Here's the list:")
    for task in enumerate(arr, start=1):
        print(f" {task[0]}| {task[1].title()}")