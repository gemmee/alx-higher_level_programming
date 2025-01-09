-- creates a table `second_table` in a db in the MySQL server and
-- adds multiple records in it.
-- description of the table: id INT, name VARCHAR(256), score INT
-- the db name is passed as an argument to the mysql command
-- if the table `second_table` exists, the script shouldn't fail
-- usage of `SELECT` or `SHOW` statements is not allowed

CREATE TABLE second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

INSERT INTO second_table
	(id, name, score)
VALUES
	(1, "John", 10),
	(2, "Alex", 3),
	(3, "Bob", 14),
	(4, "George", 8);
