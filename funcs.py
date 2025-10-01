# IMPORTS
import mysql.connector
from datetime import datetime
from rich.console import Console
from rich.table import Table


console = Console()

# Establishing Connection
con = mysql.connector.Connect(
        host = "localhost",
        user = "root",
        password = "saitharsan$5",
        database = "task"
        )
# Cursor Obejct
cur = con.cursor()

# FUNCTION 1: ADD
def add(task):
    command = f"""
    INSERT INTO {task[0]} VALUES('{task[1]}',{task[2]},'{task[3]}',{task[4]});
    """
    c = create_list(task[0])
    if c == 1:
        print("New Task List Created")
    else:
        pass
    cur.execute(command)
    con.commit()

def delete(task_list,task_name):
    command = f"""
        DELETE FROM {task_list} WHERE TASKNAME='{task_name}';
        """
    c = check_list(task_list)
    if c == 1:
        print("Task list does not exist use add command and type new tasklist to create one")
    else:
        cur.execute(command)
        con.commit()
def mark(task_name,task_list):
    command = f"""
        UPDATE {task_list}
        SET STATUS=1 WHERE TASKNAME='{task_name}';
        """
    c = check_list(task_list)
    if c == 1:
        print("Task list does not exist use add command and type new tasklist to create one")
    else:
        cur.execute(command)
        con.commit()
def unmark(task_name,task_list):
    command = f"""
        UPDATE {task_list}
        SET STATUS=0 WHERE TASKNAME='{task_name}';
        """
    c = check_list(task_list)
    if c == 1:
        print("Task list does not exist use add command and type new tasklist to create one")
    else:
        cur.execute(command)
        con.commit()

def get(task_list):
    command = f"""
        SELECT * FROM {task_list}
    """
    command2 = f"""
        SHOW TABLES;
    """
    cur.execute(command)
    task_dict = []
    for i in cur:
        task_dict.append(list(i))
    table = Table(title=f"TASKS IN {task_list}")
    table.add_column("TASKNAME", justify="center", style="green")
    table.add_column("STATUS", justify="center", style="green")
    table.add_column("DUEDATE", justify="center", style="green")
    for i in task_dict:
        if i[1] == 1:
            i[1] = "✅"
        elif i[1] == 0 and i[3] == 0:
            i[1] = "⬜"
        elif i[1] == 0 and i[3] == 1:
            i[1] = "❌"
        print(i[2].strftime("%Y-%m-%d %H:%M"))
        table.add_row(str(i[0]),str(i[1]),str(i[2].strftime("%Y-%m-%d %H:%M")))
    console.print(table)

def create_list(lst):
    command = "SHOW TABLES;"
    cur.execute(command)
    table_lst = []
    for i in cur:
        table_lst.append(i[0])
    if lst in table_lst:
        return 0
    else:
        create = f"""CREATE TABLE {lst}(
            TASKNAME VARCHAR(100),
            STATUS TINYINT(1),
            DUEDATE DATETIME,
            OVERDUE TINYINT(1)
        );"""
        cur.execute(create)
        con.commit()
        return 1
def check_list(lst):
    command = "SHOW TABLES;"
    cur.execute(command)
    table_lst = []
    for i in cur:
        table_lst.append(i[0])
    if lst in table_lst:
        return 0
    else:
        return 1
    



