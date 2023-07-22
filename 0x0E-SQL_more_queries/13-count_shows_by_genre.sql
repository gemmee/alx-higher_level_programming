-- Lists all genres from hbtn_0d_tvshows and
-- displays the number of shows linked to each
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don't display a genre that doesn't have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- You can use only one SELECT statement
SELECT DISTINCT tg.name AS genre, COUNT(ts.id) AS number_of_shows
FROM tv_show_genres AS tg
INNER JOIN tv_shows AS ts
ON tg.show_id = ts.id
ORDER BY number_of_shows DESC;

