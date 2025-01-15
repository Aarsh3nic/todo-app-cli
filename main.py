todos = []

while True:
    user_action = input("Type add, show or exit:").strip()
    match user_action:
        case "add":
            todo = input("Enter to-do:")
            todos.append(todo)
        case "show":
            for task in todos:
                print(task.title())
        case "exit":
            break
        case _:
            print("Invalid Input")


print("Bye")

