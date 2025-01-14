-- lists all shows from `hbtn_0d_tvshows_rate` db by their rating
-- each record should display: tv_shows.title - rating sum
-- results must be sorted in descending order by the rating
-- usage of more than one SELECT statement is not allowed
-- the db name is passed as an arg of the mysql command.

-- +-------------------------+
-- | Author: Gamachu         |
-- | Place: Mariyam, Shagar  |
-- +-------------------------+


SELECT ts.title, SUM(tsr.rate) rating
	FROM tv_shows ts
	INNER JOIN tv_show_ratings tsr
	ON ts.id = tsr.show_id
	GROUP BY ts.title
	ORDER BY rating DESC;
