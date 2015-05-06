#Goal: create SQLite3 databse and table
import sqlite3

conn = sqlite3.connect("new.db")

#Cursor to execute commands
cursor = conn.cursor()

cursor.execute("""CREATE TABLE population
                (city TEXT, state TEXT, population INT)
               """)

conn.close()
