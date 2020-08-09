import sqlite3

def maketable():
    connection = sqlite3.connect('bankdata.db')
    cursor = connection.cursor()

    query = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, money int)'

    cursor.execute(query)

    connection.commit()
    connection.close()
    return None