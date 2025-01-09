-- updates the score of Bob to 10 in the table `second_table`
-- Usage of Bob's id value is not allowed, only the name field is allowed
-- the db name is passed as an argument of the mysql command

UPDATE second_table SET score = 10
	WHERE name = "Bob";
