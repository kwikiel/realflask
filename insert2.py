import sqlite3
conn = sqlite3.connect("new.db")
cursor = conn.cursor()
cursor.execute('INSERT INTO population VALUES ("Paris", "France", 77000)')
conn.commit()
conn.close()
