-- Script lists all genres from a database and displays the number of shows linked to each
SELECT tv_genres.name, COUNT(tv_show_genres.show_id) AS show_count FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
GROUP BY tv_genres.name ORDER BY show_count DESC;
