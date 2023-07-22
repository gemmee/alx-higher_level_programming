-- Lists all genres from hbtn_0d_tvshows db and
-- displays the number of shows linked to each
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don't display a genre that doesn't have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- You can use only one SELECT statement
SELECT tg.name AS genre, COUNT(*) AS number_of_shows
FROM tv_show_genres tsg
INNER JOIN tv_genres tg ON tg.id = tsg.genre_id
GROUP BY tsg.genre_id
ORDER BY number_of_shows DESC;

