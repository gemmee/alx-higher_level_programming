-- lists all Comedy shows in hbtn_0d_tvshows db
-- the tv_genres table contains only one record where name = Comedy
-- each record should display: tv_shows.title
-- results must be sorted in ascending order by the show title
-- usage of more than one SELECT statement is not allowed
-- the db name is passed as an arg of the mysql command.

-- +---------------------+
-- | Author: Gamachu     |
-- | Place: occ, Kaliti  |
-- +---------------------+


SELECT tv_shows.title
	FROM tv_shows
	INNER JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
	INNER JOIN tv_genres
	ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_genres.name = 'Comedy'
	ORDER BY tv_shows.title;

-- the ff query using subquery also works but
-- it breaks the requirement by using SELECT two times
-- SELECT title
--	FROM tv_shows INNER JOIN tv_show_genres
--	ON tv_shows.id = tv_show_genres.show_id
--	WHERE tv_show_genres.genre_id = (SELECT id FROM tv_genres WHERE name = 'Comedy')
--	ORDER BY title;
