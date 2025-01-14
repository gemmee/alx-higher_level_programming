-- lists all genres not linked to the show `Dexter`
-- the tv_shows table contains only one record where title = Dexter
-- each record should display: tv_genres.name
-- results must be sorted in ascending order by the genre name
-- usage of more than two SELECT statement is not allowed
-- the db name is passed as an arg of the mysql command.

-- +---------------------+
-- | Author: Gamachu     |
-- | Place: occ, Kaliti  |
-- +---------------------+


SELECT tg.name
FROM tv_genres tg
WHERE tg.id NOT IN (	
	SELECT tg.id
	FROM tv_genres tg
	INNER JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
	INNER JOIN tv_shows ts ON tsg.show_id = ts.id
	WHERE ts.title = 'Dexter'
)
ORDER BY tg.name ASC;
