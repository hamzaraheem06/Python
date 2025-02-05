import random as r
categories = ['work', 'personal', 'study', 'finance', 'health']

def add_task(todo_tasks):
    task = {
        "task": "",
        "isCompleted": False,
        "id": None,
        "category": None
    } # defining a todo structure
    task["task"] = input("Write a todo : ") # initializing the todo task 
    task["id"] = r.randrange(1000, 5656) // r.randrange(1, 50) # generating a random id to unique tracking of a task

    add_category = input("Do you want to assign a category  ( Y or y for Yes )? ")
    if add_category.lower() == 'y':
        # providing a category option list
        for index, category in enumerate(categories):
            print(f"{index}) {category}")

        categoriy_index = len(categories) + 1
        while not(0 <= categoriy_index < len(categories)):
            try: 
                categoriy_index = int(input(f"Category index: "))
            except:
                print("Please enter an integer value.")
        
        task["category"] = categories[categoriy_index]

    todo_tasks.append(task) # adding the todo to the list
    print(f"'{task['task']}' has been added to todo list.") 

def remove_todo(todo_list):
    if not len(todo_list): # handling empty list case.
        print("The todo list is empty. No available task to be removed.")
        return 
    display_todos(todo_list) # displaying all the task to assist user
    remove_id = int(input("Enter the id of the task to be removed: ")) # knowing which one to evict
    # todo_list = [task for task in todo_list if task["id"] != remove_id] # hunting the mother fucker down

    new_list = [] # creating a new list for the updation

    for i in todo_list:
        if i["id"] == remove_id:
            print(f"'{i["task"]}' has been removed")
            continue
        new_list.append(i) # appending all the items except the one whose id matches.
    
    if len(todo_list) == len(new_list): # handling 404 case.
        print(f"No such task with id {remove_id} exist.")

    return new_list # returning the HAS RIGHTS list

# define: Filter in Python -> new_list = [expression for item in iterable if condition]

def remove_all(list):
    return list.clear()

def check_todo(todo_list):
    if not len(todo_list): # handling empty list case.
        print("Empty todo list. Cannot perform this operation")
        return

    display_todos(todo_list)
    complete_id = int(input("Enter the id of the completed task: ")) # knowing which one to tick
    for i in todo_list:
        if i["id"] == complete_id: # getting the complete task and checking if it already completed or not, otherwise mark it as complete
            if i['isCompleted']:
                print(f"'{i["task"]}' has already been marked as completed")
                return
            i["isCompleted"] = True # ticking the concerning one
            print(f"'{i["task"]}' has been marked as completed")
            return
        
    print(f"No such task with id {complete_id} exist.") # handling 404 case

def archive_task(todo_list: list, archived_list: list):
    if not len(todo_list): # handling empty list case
        print("Empty todo list. Cannot perform this operation")
        return

    display_todos(todo_list) # displaying the list to assit the user for selection
    complete_id = int(input("Enter the id of the task: ")) # knowing which one to tick
    for i in todo_list:
        if i["id"] == complete_id:
            archived_list.append(i) # using apped because it is a single item, and not a sequence.
            print(f"'{i["task"]}' has been moved to archive.")
            todo_list.remove(i) # removing from the main list
            return todo_list, archived_list # returning the updated list
        
    print(f"No such task with id {complete_id} exist.") # handling 404 case

def mark_all(todo_list):
    if not len(todo_list): # handling the empty list case
        print("Empty todo list. Cannot perform this operation")
        return
    
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
    if not len(todo_list): # handling emtpy list case
        print("Empty todo list. Cannot perform this operation")
        return
    
    display_todos(todo_list) # displaying the list to assist user
    change_id = int(input("Enter the id of the task to be changed: "))

    for i in todo_list:
        if i["id"] == change_id: 
            i["task"] = input("Enter the changes: ") # getting the changed task
            i["isCompleted"] = False # since the task has been changed, we check it as incomplete
            print("Changes have been saved.")
            return 

    print(f"No such task with id {change_id} exist.") # handling the 404 case

def display_todos(todo_list):
    if not len(todo_list): # handling the empty list case
        print("Empty todo list.")
        return

    print(f"{'ID':<10} {'Task':<50} {'Completed':<10} {'Category':<10}") # :<10 is left-align, used to set character lenght of a string
    print("-" * 81) # header underline

    for i in todo_list:
        category = "N/A" if not i["category"] else i["category"]
        print(f"{str(i['id']):<10} {i['task']:<50} {str(i['isCompleted']):<10} {category:<10}")
    # using a for each loop to display the task information

def remove_completed_todos(todo_list):
    return [task for task in todo_list if not task["isCompleted"]] # self explanatory

def archive_complete(todo_list):
    return [task for task in todo_list if task["isCompleted"]] # self explanatory

def show_statistics(todo_list, archived_list):
    if not len(todo_list): # handling the empty list case
        print("Empty todo list.")
        return

    is_archived_included = input("Do you want to include the archived list in the statistics ( Y or y for Yes )? ") 

    all_tasks = todo_list + (archived_list if is_archived_included.lower() == 'y' else [])

    total_tasks = len(all_tasks)
    
    completed_tasks = 0
    category_wise_count = [{"count": 0, "completed": 0} for _ in categories]
    uncat_task = {"count": 0, "completed": 0}
    for i in all_tasks:
        if not i['category']:
            uncat_task["count"] += 1
            if i['isCompleted']:
                uncat_task["completed"] += 1
                completed_tasks += 1
            continue
        
        category_index = categories.index(i['category']) # instead of hardcoding the index, we get the index everytime for a task and then categorize it.
        category_wise_count[category_index]["count"] += 1
        if i['isCompleted']:
            category_wise_count[category_index]["completed"] += 1
            completed_tasks += 1

    pending_tasks = total_tasks - completed_tasks

    # displaying the stats
    print(f"\nTotal tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}  ({round(completed_tasks / total_tasks, ndigits=2) * 100})")
    print(f"Pending tasks: {pending_tasks}  ({round((pending_tasks / total_tasks) , ndigits=2) * 100})")

    # displaying the categorized stats

    print("\nCategorized Statistics: \n")

    for i in range(0, len(categories)):
        print(
    f"{categories[i].title():<15} : "
    f"{category_wise_count[i]['count']:>3} Task(s), "
    f"{category_wise_count[i]['completed']:>3} Completed, "
    f"{(category_wise_count[i]['count'] - category_wise_count[i]['completed']):>3} Pending."
)

    else:
        print(
    f"{'Uncategorized':<15} : "
    f"{uncat_task['count']:>3} Task(s), "
    f"{uncat_task['completed']:>3} Completed, "
    f"{(uncat_task['count'] - uncat_task['completed']):>3} Pending."
)


# todo: https://chatgpt.com/c/678e22da-53cc-800a-a1ad-d4eadb1ad6cb

def help():
    print(
    "\n"
    "a)  Add a task\n"
    "r)  Remove a task\n"
    "c)  Check a task\n"
    "at) Archive a task\n"
    "ma) Mark all as incomplete/complete\n"
    "ch) Change a task\n"
    "d)  Display todos\n"
    "ac) Archive completed tasks\n"
    "da) Display archived tasks\n"
    "rc) Remove completed tasks\n"
    "ct) Clear tasks\n"
    "ca) Clear archive\n"
    "ss) Show statistics\n"
    "h)  Help\n"
    "e)  Exit\n"
)


def main(): # creating the user interface
    todo_tasks = []
    archived_tasks = []
    print("Todo List:")
    print('~' * len("Todo List:"))
    print(
    "\n"
    "a)  Add a task\n"
    "r)  Remove a task\n"
    "c)  Check a task\n"
    "at) Archive a task\n"
    "ma) Mark all as incomplete/complete\n"
    "ch) Change a task\n"
    "d)  Display todos\n"
    "ac) Archive completed tasks\n"
    "da) Display archived tasks\n"
    "rc) Remove completed tasks\n"
    "ct) Clear tasks\n"
    "ca) Clear archive\n"
    "ss) Show statistics\n"
    "h)  Help\n"
    "e)  Exit\n"
)

    choice = None
    while choice != 'e':
        choice = input("Your choice? ")
        match choice:
            case 'a':
                add_task(todo_tasks)
            case 'r':
                todo_tasks = remove_todo(todo_tasks)
            case 'c':
                check_todo(todo_tasks)
            case 'at':
                todo_tasks, archived_tasks = archive_task(todo_tasks, archived_tasks)
            case 'ma':
                mark_all(todo_tasks)
            case 'ch':
                change_todo(todo_tasks)
            case 'd':
                display_todos(todo_tasks)
            case 'rc':
                todo_tasks = remove_completed_todos(todo_tasks)
                print("The completed tasks have been removed from the todo list.")
            case 'ct':
                todo_tasks = remove_all(todo_tasks)
                print("The todo list has been cleared.")
            case 'ca':
                archived_tasks = remove_all(archived_tasks)
                print("The archived list has been cleared.")
            case 'ac':
                new_archived = archive_complete(todo_tasks)  # Archive completed tasks
                archived_tasks.extend(new_archived) # adding the new archived to the existing list
                # note: using extend because append will add the new archived as a whole list in the archived_list. on the other hand, extend adds the elements individually in the list
                todo_tasks = remove_completed_todos(todo_tasks) # removing the complete from the original list
                print("The completed tasks have been moved to the archived list.")
            case 'da':
                display_todos(archived_tasks)
            case 'ss':
                show_statistics(todo_list=todo_tasks, archived_list=archived_tasks)
            case 'h':
                help()
            case 'e':
                print("....exiting")
            case _:
                print("Invalid operation.😬")
main()