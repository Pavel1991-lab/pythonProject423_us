

INSERT INTO genres(name)
VALUES ('Horor'), ('Sci-Fi');

INSERT INTO  author(name)
VALUES ('Author_1'), ('Author_2'), ('Author_3');

INSERT INTO  books (name, genre_id)
VALUES ('Book_1', 1), ('Book_2', 2), ('Book_3', 2);

INSERT INTO book_author(book_id, author_id)
VALUES (1, 1), (2, 1), (2, 3);