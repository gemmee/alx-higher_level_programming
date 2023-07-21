-- List all shows in db 'hbtn_0d_tvshows'
-- Each record show display tv_shows.title, tv_show_genres.genre_id
-- If show doesn't have genre, display NULL
-- You can use only one SELECT statement
SELECT ts.title, tg.genre_id
FROM tv_shows AS ts LEFT JOIN tv_show_genres AS tg
ON ts.id = tg.show_id
ORDER BY ts.title, tg.genre_id;
