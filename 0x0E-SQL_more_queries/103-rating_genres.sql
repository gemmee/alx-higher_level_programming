-- lists all genres from `hbtn_0d_tvshows_rate` db by their rating
-- each record should display: tv_genres.name - rating sum
-- results must be sorted in descending order by the rating
-- usage of more than one SELECT statement is not allowed
-- the db name is passed as an arg of the mysql command.

-- +-------------------------+
-- | Author: Gamachu         |
-- | Place: Mariyam, Shagar  |
-- +-------------------------+


SELECT tg.name, SUM(tsr.rate) rating
	FROM tv_genres tg
	INNER JOIN tv_show_genres tsg
	ON tg.id = tsg.genre_id
	INNER JOIN tv_show_ratings tsr
	ON tsg.show_id = tsr.show_id
	GROUP BY tg.name
	ORDER BY rating DESC;
