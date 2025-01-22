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


def remove_todo(todo_list):
    remove_id = int(input("Enter the id of the task to be removed: ")) # knowing which one to evict
    todo_list = [task for task in todo_list if task["id"] != remove_id] # hunting the mother fucker down
    print(f"The task with id {remove_id} has been removed")
    return todo_list # returning the HAS RIGHTS list
            
# define: Filter in Python -> new_list = [expression for item in iterable if condition]


def check_todo(todo_list):
    complete_id = int(input("Enter the id of the completed task: ")) # knowing which one to tick
    for i in todo_list:
        if i["id"] == complete_id:
            i["isCompleted"] = True # ticking the concerning one
            print(f"'{i["task"]}' has been marked as completed")
            return
        
    print(f"No such task with id {complete_id} exist.")

def mark_all(todo_list):
    choice = input("Mark as: \n'T' or 't' for complete\n'F' or 'f' for incomplete\n")
    
    match choice:
        case 'T' | 't':
            for i in todo_list:
                i["isCompleted"] = True if not i["isCompleted"] else i["isCompleted"] # set it as True if it is False, otherwise let it be unchanged
            print("Marked all as completed.")
        case 'F' | 'f':
            for i in todo_list:
                i["isCompleted"] = False if i["isCompleted"] else i["isCompleted"] # set it as False if it is True, otherwise let it be unchanged
            print("Marked all as incompleted.")
        case _:
            print("Invalid operation.😬")


def change_todo(todo_list):
    change_id = int(input("Enter the id of the task to be changed: "))

    for i in todo_list:
        if i["id"] == change_id:
            i["task"] = input("Enter the changes: ") # getting the changed task
            i["isCompleted"] = False # since the task has been changed, we check it as incomplete
            print("Changes have been saved.")
            return 

    print(f"No such task with id {change_id} exist.")

def display_todos(todo_list):
    if len(todo_list) == 0:
        print("Empty todo list.")
        return

    print(f"{'ID':<10} {'Task':<50} {'Completed':<10}") # :<10 is left-align, used to set character lenght of a string
    print("-" * 71) # header underline

    for i in todo_list:
        print(f"{str(i['id']):<10} {i['task']:<50} {str(i['isCompleted']):<10}")
    # using a for each loop to display the task information


def remove_completed_todos(todo_list):
    return [task for task in todo_list if not task["isCompleted"]]

# todo: https://chatgpt.com/c/678e22da-53cc-800a-a1ad-d4eadb1ad6cb

def help():
    print("\na) Add a task\nr) Remove a task \nc) Check a task\nma) Mark all as incomplete/complete\nch) Change a task\nd) Display todos\nrc) Remove completed tasks\nh) Help\nq) Exit\n")

def main(): # creating the user interface
    todo_tasks = []
    print("Todo List:")
    print("\na) Add a task\nr) Remove a task \nc) Check a task\nma) Mark all as incomplete/complete\nch) Change a task\nd) Display todos\nrc) Remove completed tasks\nh) Help\nq) Exit\n")
    choice = None
    while choice != 'q':
        choice = input("Your choice? ")
        match choice:
            case 'a':
                add_task(todo_tasks)
            case 'r':
                display_todos(todo_tasks)
                todo_tasks = remove_todo(todo_tasks)
            case 'c':
                display_todos(todo_tasks)
                check_todo(todo_tasks)
            case 'ma':
                mark_all(todo_tasks)
            case 'ch':
                display_todos(todo_tasks)
                change_todo(todo_tasks)
            case 'd':
                display_todos(todo_tasks)
            case 'rc':
                todo_tasks = remove_completed_todos(todo_tasks)
                print("The completed tasks have been removed from the todo list.")
            case 'h':
                help()
            case 'q':
                print("....quiting")
            case _:
                print("Invalid operation.😬")
main()