#INSERT Command
#Import sqlite3
import sqlite3
#Create connection object
conn = sqlite3.connect("new.db")
#Get a cursor object used to execute SQL commands
cursor = conn.cursor()
#Insert data
cursor.execute('INSERT INTO population VALUES ("Yolocity", "Animeland", 404)')
#Commit the change
conn.commit()
#Close the database connection
conn.close()
