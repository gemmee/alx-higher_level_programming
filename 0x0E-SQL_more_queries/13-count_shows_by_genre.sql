-- lists all genres from hbtn_0d_tvshows db and
-- displays the number of shows linked to each
-- each record should display: <TV show genre> - <Number of shows linked to this genre>
-- first column must be called `genre`
-- second column must be called `number_of_shows`
-- genres with no shows linked should not be displayed
-- results must be sorted in descending order by the number of shows linked
-- usage of more than one SELECT statement is not allowed
-- the db name is passed as an arg of the mysql command.

-- +---------------------+
-- | Author: Gamachu     |
-- | Place: occ, Kaliti  |
-- +---------------------+

SELECT name AS genre, COUNT(*) AS number_of_shows
	FROM tv_genres INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
	GROUP BY genre
	ORDER BY number_of_shows DESC;
