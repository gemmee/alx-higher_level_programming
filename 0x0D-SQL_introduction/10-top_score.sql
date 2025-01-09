-- lists all records of the table `second_table`
-- the db name is passed as an argument of the mysql command
-- records should be ordered by score (top first)
-- results should display both the score and the name (in this order)

SELECT score, name FROM second_table ORDER BY score DESC;
