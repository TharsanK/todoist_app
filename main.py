# IMPORTS
import csv

# Possible Commands
HELP = """
Welcome to help: Here are all the commands you can use
help: prints this message
add: adds a new task
delete: deletes a task
mark: marks a task as done
unmark: unmarks a as undone
get: get all the tasks
"""
# Welcome to app message
print()
print("WELCOME TO TERMINAL TODOIST: An App for Student Productivity")
# Print Help Message at the start of app
print(HELP)
# Handling User Input

while True:
    cmd = input(">>>")
