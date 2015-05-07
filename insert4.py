import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    cities = [
            ('Boston', 'MA', 60000),
            ('Chicago', 'IL', 12345),
            ('SimCity', 'GAME', 5)
            ]
    c.executemany('INSERT INTO POPULATION VALUES(?,?,?)', cities)
