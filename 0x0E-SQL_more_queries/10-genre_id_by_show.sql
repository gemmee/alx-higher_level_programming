-- List all shows in 'hbtn_0d_tvshows' that have at least one genre linked
-- Each record should display
-- tv_shows.title, tv_show_genres.genre_id
-- Sort the result in ascending order by tv_shows.title and
-- tv_show_genres.genre_id
-- You can only use one SELECT statement
SELECT ts.title, tg.genre_id FROM tv_show_genres AS tg
JOIN tv_shows AS ts ON tg.show_id = ts.id
ORDER BY ts.title, tg.genre_id;
