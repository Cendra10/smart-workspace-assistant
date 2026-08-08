import sqlite3

connection = sqlite3.connect(
    "smart_workspace.db",
    check_same_thread=False)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)
""")
def create_task(title):
    cursor.execute("""
    INSERT INTO tasks (title)
    VALUES (?)
    """, 
    (title,))

    connection.commit()



def update_task(task_id, task_title):
    cursor.execute(
        "UPDATE tasks SET title = ? WHERE id=?",
        (task_title, task_id)
)
    connection.commit()

def delete_task(task_id):
    cursor.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
)

    connection.commit()

def get_all_tasks():
    cursor.execute(
        "SELECT * FROM tasks"
)

    rows = cursor.fetchall()

    return rows

def get_task(task_id):
    cursor.execute(
        "SELECT * FROM tasks WHERE id=?",
        (task_id,)
    )

    rows = cursor.fetchone()
    return rows