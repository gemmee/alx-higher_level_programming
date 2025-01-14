-- lists all shows and all genres linked to that show in hbtn_0d_tvshows db
-- for a show that doesn't have a genre, NULL is dispayed in genre column
-- each record should display: tv_shows.title - tv_genres.name
-- results must be sorted in ascending order by the show title and genre name
-- usage of more than one SELECT statement is not allowed
-- the db name is passed as an arg of the mysql command.

-- +---------------------+
-- | Author: Gamachu     |
-- | Place: occ, Kaliti  |
-- +---------------------+


SELECT title, name
	FROM tv_shows AS ts
	LEFT JOIN tv_show_genres AS tsg
	ON ts.id = tsg.show_id
	LEFT JOIN tv_genres AS tg
	ON tg.id = tsg.genre_id
	ORDER BY title, name;
