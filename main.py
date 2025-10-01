# IMPORTS
import funcs
from datetime import datetime
# Possible Commands
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
# Welcome to app message
print()
print("WELCOME TO TERMINAL TODOIST: An App for Student Productivity")
# Print Help Message at the start of app
print(HELP)
# Handling User Input

while True:
    cmd = input(">>>")
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
    elif cmd.lower() == "delete":
        task_name = input("Enter task name: ")
        task_list = input("Enter the name of the list: ")
        funcs.delete(task_list,task_name)
    elif cmd.lower() == "delete tasklist":
        task_list = input("Enter task list name: ")
        funcs.delete_task_list(task_list)
    elif cmd.lower() == "mark":
        task_name = input("Enter task name: ")
        task_list = input("Enter the name of the list: ")
        funcs.mark(task_name,task_list)
    elif cmd.lower() == "unmark":
        task_name = input("Enter task name: ")
        task_list = input("Enter the name of the list: ")
        funcs.unmark(task_name,task_list)
    elif cmd.lower() == "get":
        task_list = input("Enter task list name or Click Enter to get all task list1: ")
        funcs.get(task_list)
    


    elif cmd.lower() == "exit":
        break
