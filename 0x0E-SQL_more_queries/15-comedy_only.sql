-- Lists all Comedy shows in the db hbtn_0d_tvshows
-- 'tv_genres' table contains only one record where name = Comedy
-- (but id can be different)
-- Results must be sorted in ascending order by the show title
-- You can only use one SELECT statement
SELECT ts.title
FROM tv_shows ts
INNER JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
INNER JOIN tv_genres tg
ON tg.id = tsg.genre_id
WHERE tg.name = 'Comedy'
ORDER BY ts.title;
