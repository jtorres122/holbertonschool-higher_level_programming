-- Script lists all comedy shows in a database
SELECT tv_shows.title FROM tv_shows
INNER JOIN tv_show_genres ON tv_genres.id=tv_show_genres.id
INNER JOIN tv_shows ON tv_shows.id=tv_show_genres.id
WHERE tv_genres.name='Comedy'
ORDER BY tv_shows.title ASC;
