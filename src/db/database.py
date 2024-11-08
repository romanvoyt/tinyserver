import sqlite3
from config import DATABASE_NAME

def connect_db():
    return sqlite3.connect(DATABASE_NAME)

def init_db():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS users (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       age INTEGER NOT NULL
                       )
                       """)
        conn.commit()

def create_user(name, age):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
        return cursor.lastrowid

def get_user(id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        return cursor.fetchone()
    
def get_all_users():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()

def update_user(id, name, age):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, id))
        conn.commit()
        return cursor.rowcount

def delete_user(id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (id,))
        conn.commit()
        return cursor.rowcount

