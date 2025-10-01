# REQUIRED IMPORTS
import funcs
from datetime import datetime

# USER HELP
HELP = """
Welcome to help: Here are all the commands you can use
help: prints this message
add: adds a new task
delete: deletes a task
mark: marks a task as done
unmark: unmarks a as undone
get: get all the tasks
delete tasklist: delete a tasklist
exit: to exit the app
"""
# WELCOME TO THE APP MESSAGE
print()
print("WELCOME TO TERMINAL TODOIST: An App for Student Productivity")

# PRINTS HELP MESSAGE AT THE START OF THE PROGRAM
print(HELP)

# DATABASE UPDATION TO MATCH THE SYSDATE
funcs.update_database()

# HANDLING USER INPUT
# THIS IS A TERMINAL/COMMAND LINE BASED APP WITH USER COMMAND IT DOES NOT HAVE GUI(GRAPHICAL USER INTERFACE)
while True:
    # MAKING IT LOOK LIKE THE TERMINAL
    cmd = input(">>>")

    #  THE HELP FUNCTIONALITY
    if cmd.lower() == "help":
        print(HELP)

    # THE ADD FUNCTIONALITY
    if cmd.lower() == "add":
        t_lst = input("Enter Tasklist Name: ")
        t_name = input("Enter Task Name: ")
        t_status = 0
        day = int(input('Enter Date: '))
        month = int(input('Enter month: '))
        year = int(input('Enter year: '))
        time_h = int(input('Enter time hours(24 hour format): '))
        time_m = int(input('Enter time minutes: '))
        date = datetime(year,month,day,time_h,time_m)
        if datetime.now() >= date:
            overdue = 1
        else:
            overdue = 0
        lst = [t_lst,t_name,t_status,date,overdue]
        funcs.add(lst)
        print("Successfully Added")
    
    # THE DELETE FUNCTIONALITY
    elif cmd.lower() == "delete":
        task_name = input("Enter task name: ")
        task_list = input("Enter the name of the list: ")
        funcs.delete(task_list,task_name)
    
    # THE DELETE TASKLIST FUNCTIONALITY
    elif cmd.lower() == "delete tasklist":
        task_list = input("Enter task list name: ")
        funcs.delete_task_list(task_list)

    # THE MARK FUNCTIONALITY
    elif cmd.lower() == "mark":
        task_name = input("Enter task name: ")
        task_list = input("Enter the name of the list: ")
        funcs.mark(task_name,task_list)
    
    # THE UNMARKS FUNCTIONALITY
    elif cmd.lower() == "unmark":
        task_name = input("Enter task name: ")
        task_list = input("Enter the name of the list: ")
        funcs.unmark(task_name,task_list)
    
    # THE GET ALL FUNCTIONALITY
    elif cmd.lower() == "get":
        funcs.get()
    
    # THE EXIT FUNCTIONALITY
    elif cmd.lower() == "exit":
        break

# NOTE: THE REQUIRED FUNCTIONS USED IN THIS PROJECT ARE IN THE funcs.py FILE PLEASE REFER
