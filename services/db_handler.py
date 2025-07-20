
import sqlite3

DB_PATH = "database/citizen.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def insert_citizen(perID, name, dob, sex):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO citizen VALUES (?, ?, ?, ?)", (perID, name, dob, sex))
    conn.commit()
    conn.close()

def update_citizen(perID, name=None, dob=None, sex=None):
    conn = get_connection()
    cursor = conn.cursor()
    fields = []
    values = []
    if name:
        fields.append("name=?")
        values.append(name)
    if dob:
        fields.append("dob=?")
        values.append(dob)
    if sex:
        fields.append("sex=?")
        values.append(sex)
    values.append(perID)
    cursor.execute(f"UPDATE citizen SET {', '.join(fields)} WHERE perID=?", values)
    conn.commit()
    conn.close()

def delete_citizen(perID):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM citizen WHERE perID=?", (perID,))
    conn.commit()
    conn.close()

def search_by_perID(perID):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM citizen WHERE perID=?", (perID,))
    result = cursor.fetchone()
    conn.close()
    return result

def search_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM citizen WHERE name LIKE ?", (f"%{name}%",))
    results = cursor.fetchall()
    conn.close()
    return results
