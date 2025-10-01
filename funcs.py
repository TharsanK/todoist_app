# IMPORTS
import mysql.connector
from datetime import datetime
from rich.console import Console
from rich.table import Table

# CREATING RICH CONSOLE
console = Console()

# ESTABLISHING CONNECTION TO MYSQL
con = mysql.connector.Connect(
        host = "localhost",
        user = "root",
        password = "saitharsan$5",
        database = "task"
        )

# CURSOR OBJECT
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

# FUNCTION 2: DELETE
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

# FUNCTION 3: MARK
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

# FUNCTION 4: UNMARK
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

# FUNCTION 5: GET
def get():
    command2 = f"""
        SHOW TABLES;
    """
    cur.execute(command2)
    table_lst = []
    for i in cur:
        table_lst.append(i[0])
    print(table_lst)
    for i in table_lst:
        command = f"""
            SELECT * FROM {i}
        """
        cur.execute(command)
        task_dict = []
        for j in cur:
            task_dict.append(list(j))
        table = Table(title=f"TASKS IN {i}")
        table.add_column("TASKNAME", justify="center", style="green")
        table.add_column("STATUS", justify="center", style="green")
        table.add_column("DUEDATE", justify="center", style="green")
        for k in task_dict:
            if k[1] == 1:
                k[1] = "✅"
            elif k[1] == 0 and k[3] == 0:
                k[1] = "⬜"
            elif k[1] == 0 and k[3] == 1:
                k[1] = "❌"
            table.add_row(str(k[0]),str(k[1]),str(k[2].strftime("%Y-%m-%d %H:%M")))
        console.print(table)

# FUNCTION 6: DELETE TASK LIST
def delete_task_list(task_list):
    command = f"""
    DROP TABLE {task_list};
    """
    c = check_list(task_list)
    if c == 1:
        print("Task list does not exist")
    else:
        cur.execute(command)
        con.commit

# FUNCTION 7: CREATE LIST FUNCTION --> LINKED AND USED IN FUNCTION 1: ADD 
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
# FUNCTION 8: CHECK LIST --> LINKED AND USED IN MARK,UNMARK,DELETE,DELETE TASKLIST,GET
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
def update_database():
    cmd1 = f"""
    SHOW TABLES;
    """
    cur.execute(cmd1)
    table_lst = []
    for i in cur:
        table_lst.append(i[0])
    for i in table_lst:
        cmd2 = f"""
        UPDATE {i}
        SET OVERDUE = 1 
        WHERE DUEDATE < SYSDATE();
        """
        cur.execute(cmd2)
        con.commit()

    



