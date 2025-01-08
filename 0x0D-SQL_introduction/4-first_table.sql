-- creates a table called `first_table` in the current db in the MySQL server
-- the db name is passed as arg of the mysql command
-- if the table `first_table` exists, the script should not fail
-- Usage of `SELECT` or `SHOW` statements is not allowed

CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
