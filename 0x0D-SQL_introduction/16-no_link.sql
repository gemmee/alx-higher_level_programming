-- lists those records of the table `second_table` with
-- a `name` value, i.e. doesn't list rows without a `name` value
-- results should display the score and the name (in this order)
-- records should be listed by descending score
-- the db name is passed as an argument to the mysql command

SELECT score, name FROM second_table
	WHERE name IS NOT NULL
	ORDER BY score DESC;
