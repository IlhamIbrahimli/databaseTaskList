import sqlite3

class TaskManager:
    def __init__(self,database):
        self.database = database


    def create_table(self,table_name,parameters: str):
        self.table_name = table_name
        con = sqlite3.connect(self.database)
        with con:
            cur = con.cursor()
            cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name}{parameters}")
            con.commit()
            cur.close()

    def add_task(self, user_id: int, name: str, description: str):
        con = sqlite3.connect(self.database)
        with con:
            cur = con.cursor()
            cur.execute(f"INSERT INTO {self.table_name} values(?,?,?,?)", (None,name,description,user_id))
            con.commit()
            cur.close()

    def delete_task(self, task_name: str):
        con = sqlite3.connect(self.database)
        with con:
            con.execute(f"DELETE FROM {self.table_name} WHERE task = ?", (task_name, ))
            con.commit()

    def show_task(self,user_id):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(f"SELECT task FROM {self.table_name} WHERE user_id = ?", (user_id,))
            return cur.fetchall()
    
Tsk = TaskManager("tasklist.db") #Change this to whatever you want
#Always run create_table even if table already exists so it can set table_name for future use.
Tsk.create_table("tasks","(id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT NOT NULL, desc TEXT, user_id INTEGER)") # Create tasks table

#Add 2 placeholder tasks
Tsk.add_task(1234,"Do foo", "Foo is very important!!!")

Tsk.add_task(1234,"Do foo2", "Foo2 is also very important!!!")
Tsk.delete_task("Do foo") # Delete placeholder task 1