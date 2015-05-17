import sqlite3

def read(cursor):
    """
    (u'Warsaw', u'Mazowieckie', 1337)
    (u'Berlin', u'Germany', 9001)
    (u'Tokio', u'Japan', 555)
    (u'Yolocity', u'Animeland', 404)
    (u'Paris', u'France', 77000)
    (u'New York', u'USA', 890)
    (u'New York', u'USA', 890)
    (u'Boston', u'MA', 60000)
    (u'Chicago', u'IL', 12345)
    (u'SimCity', u'GAME', 5)

    """
    cur = cursor.execute("SELECT * from population")

    for data in cur:
        print data

conn = sqlite3.connect("new.db")
cursor = conn.cursor()
read(cursor)
