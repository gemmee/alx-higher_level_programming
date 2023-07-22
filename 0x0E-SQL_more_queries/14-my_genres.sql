-- Lists all genres of the show Dexter from hbtn_0d_tvshows db
-- The tv_shows table contains only one record where title = Dexter
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use only one SELECT statement
SELECT tg.name FROM tv_genres tg 
INNER JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
INNER JOIN tv_shows ts ON tsg.show_id = ts.id
WHERE ts.title = 'Dexter'
ORDER BY tg.name;
