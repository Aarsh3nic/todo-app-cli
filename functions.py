FILEPATH = "todos.txt"

def display():
    """Reads and displays the list present in the text file"""

    taskList = getTaskList()
    print("Here's the list:")
    for task in enumerate(taskList, start=1):
        print(f" {task[0]}| {task[1]}",end="")


def modifyText(taskList, message,filePath=FILEPATH):
    """Writes the given list to the text file"""

    with open(filePath, "w") as file:
        file.writelines(taskList)
    print(message)

def getTaskList(filePath=FILEPATH):
    """Returns the list of todos from the given text file"""

    with open(filePath, "r") as file: 
        taskList = file.readlines()
        return taskList
