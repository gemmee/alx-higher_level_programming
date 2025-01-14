-- lists all genres of the show `Dexter` in hbtn_0d_tvshows db
-- each record should display: tv_genres.name
-- results must be sorted in ascending order by the genre name
-- usage of more than one SELECT statement is not allowed
-- the db name is passed as an arg of the mysql command.

-- +---------------------+
-- | Author: Gamachu     |
-- | Place: occ, Kaliti  |
-- +---------------------+

SELECT name
	FROM tv_genres INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_show_genres.show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter')
	ORDER BY name;
