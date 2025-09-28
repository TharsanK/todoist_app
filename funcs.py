# Basic Imports
import csv

# Function 1: Add: Adds a new task to the list
def add(task_data):
    with open("data.csv","a+") as cf:
        mywrite = csv.writer(cf,delimiter=",")
        mywrite.writerow(task_data)
