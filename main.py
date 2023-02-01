import sqlite3

with sqlite3.connect("books_db.sqlite") as connection:
    cursor = connection.cursor()

    cursor.execute()
