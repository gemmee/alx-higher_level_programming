-- lists all shows contained in `hbtn_0d_tvshows` that have
-- at least one genre linked
-- each record should display: tv_shows.title - tv_show_genres.genre_id
-- results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- usage of more than one SELECT statement is not allowed
-- the db name is passed as an arg of the mysql command.

-- +---------------------+
-- | Author: Gamachu     |
-- | Place: occ, Kaliti  |
-- +---------------------+

SELECT title, genre_id
	FROM tv_shows INNER JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
	ORDER BY tv_shows.title, tv_show_genres.genre_id;
