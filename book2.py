import sqlite3

with sqlite3.connect("books_db.sqlite") as connection:
    cursor = connection.cursor()


    query = """
       CREATE TABLE books_3(
       id integer PRIMARY KEY AUTOINCREMENT, 
       name varchar(40) NOT NULL,
       author varchar(80),
       description varchar(255),
       genre varchar(20) CONSTRAINT df_genre DEFAULT 'Underfined',
       publication_date date,
       page_count integer CONSTRAINT  ck_page_count CHECK (page_count>0) ,
       price decimal ) 
    """

    #cursor.execute(query)

    query = """
       DELETE FROM books_3
       WHERE PRICE < 130
    """
    cursor.execute(query)

