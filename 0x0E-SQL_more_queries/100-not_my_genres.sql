-- Use 'hbtn_0d_tvshows' db to list all genres not linked to 'Dexter' show
-- 'tv_shows' table contains only one record where title = 'Dexter'
-- Each record should display tv_genres.name
-- Results must be sorted in ascending order by genre name
-- You can use max of two SELECT statements
SELECT g.name
FROM tv_genres g
WHERE g.name NOT IN (
	SELECT g.name
	FROM tv_genres g
	INNER JOIN tv_show_genres sg ON g.id = sg.genre_id
	INNER JOIN tv_shows s ON sg.show_id = s.id
	WHERE s.title = 'Dexter'
)
ORDER BY g.name ASC;
