# IMPORTS
import mysql.connector
from datetime import datetime

# Establishing Connection
con = mysql.connector.Connect(
        host = "localhost",
        user = "root",
        password = "saitharsan5",
        database = "task"
        )
# Cursor Obejct
cur = con.cursor()

# FUNCTION 1: ADD
def add(task):
    command = f"""
    INSERT INTO {task[0]} VALUES('{task[1]}',{task[2]},'{task[3]}',{task[4]});"""
    cur.execute(command)
    con.commit()


