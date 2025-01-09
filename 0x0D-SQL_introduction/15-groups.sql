-- lists the number of records with the same score in the table `second_table`
-- the result should display the score and
-- the number of records for this score with the label number
-- the list should be sorted by the number of records (descending)
-- the db name is passed as an argument to the mysql command

SELECT score, COUNT(score) AS number FROM second_table
	GROUP BY score
	ORDER BY number DESC;
