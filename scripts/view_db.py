import sqlite3

conn = sqlite3.connect("database/citizen.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM citizen LIMIT 10")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

