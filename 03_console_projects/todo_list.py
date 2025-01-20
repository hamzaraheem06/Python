import random as r

def add_task(todo_tasks):
    task = {
        "task": "",
        "isCompleted": False,
        "id": None
    } # defining a todo structure
    task["task"] = input("Write a todo : ")
    task["id"] = r.randrange(1000, 5656) // r.randrange(1, 50) # initializing the todo task

    todo_tasks.append(task) # adding the todo to the list
    print(f"'{task['task']}' has been added to todo list.")


def display_todos(todo_list):
    if len(todo_list) == 0:
        print("Empty todo list. Loser😒.")
        return

    print(f"{'ID':<10} {'Task':<35} {'Completed':<10}") # :<10 is left-align, used to set character lenght of a string
    print("-" * 56)

    for i in todo_list:
        print(f"{str(i['id']):<10} {i['task']:<35} {str(i['isCompleted']):<10}")
 # using a for each loop to display the task information


def remove_todo(todo_list):
    remove_id = int(input("Enter the id of task to be removed: ")) # knowing which one to evict
    todo_list = [task for task in todo_list if task["id"] != remove_id] # hunting the mother fucker down
    return todo_list # returning the HAS RIGHTS list
            
# define: Filter in Python -> new_list = [expression for item in iterable if condition]

def check_todo(todo_list):
    complete_id = int(input("Enter the id of the completed task: ")) # knowing which one to tick
    for i in todo_list:
        if i["id"] == complete_id:
            i["isCompleted"] = True # ticking the concerning one
            return

def main(): # creating the user interface
    todo_tasks = []
    print("Todo List:")
    print("\na) Add a task\nr) Remove a task \nc) Check a task\nch) Change a task\nd) Display todos\nq) Exit\n")
    choice = None
    while choice != 'q':
        choice = input("Your choice? ")
        match choice:
            case 'a':
                add_task(todo_tasks)
            case 'r':
                todo_tasks = remove_todo(todo_tasks)
            case 'c':
                check_todo(todo_tasks)
            case 'ch':
                print("....changing a task")
            case 'd':
                display_todos(todo_tasks)
            case 'q':
                print("....quiting")
            case _:
                print("Invalid operation: 😬😬")
main()