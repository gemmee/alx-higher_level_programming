-- lists all shows without the genre Comedy in the db
-- the tv_genres table contains only one record where name = Comedy
-- each record should display: tv_shows.title
-- results must be sorted in ascending order by the show title
-- usage of more than two SELECT statement is not allowed
-- the db name is passed as an arg of the mysql command.

-- +-------------------------+
-- | Author: Gamachu         |
-- | Place: Mariyam, Shagar  |
-- +-------------------------+


SELECT ts.title
FROM tv_shows ts
WHERE ts.id NOT IN (	
	SELECT ts.id
	FROM tv_shows ts
	INNER JOIN tv_show_genres tsg ON ts.id = tsg.show_id
	INNER JOIN tv_genres tg ON tsg.genre_id = tg.id
	WHERE tg.name = 'Comedy'
)
ORDER BY ts.title ASC;
