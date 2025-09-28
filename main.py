# IMPORTS
import csv
import funcs as f
from datetime import date

# Possible Commands
HELP = """
Welcome to help: Here are all the commands you can use
help: prints this message
add: adds a new task
delete: deletes a task
mark: marks a task as done
unmark: unmarks a as undone
get: get all the tasks
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
        t_name = input("Enter task name: ")
        t_status = False
        t_due_date = int(input("Enter date: "))
        t_due_month = int(input("Enter month: "))
        t_due_year = int(input("Enter year: "))
        due_date = date(t_due_year,t_due_month,t_due_date)
        overdue = False
        f.add([t_name,t_status,due_date,overdue])
    elif cmd.lower() == "exit":
        break
