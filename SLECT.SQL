SELECT books.name as 'book_name', genres.name as 'genres.name' from books
INNER JOIN genres ON
genre_id = genres.id
