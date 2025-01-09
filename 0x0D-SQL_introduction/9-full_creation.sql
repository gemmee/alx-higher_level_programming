-- creates a table `second_table` in a db in the MySQL server and
-- adds multiple records in it.
-- description of the table: id INT, name VARCHAR(256), score INT
-- the db name is passed as an argument to the mysql command
-- if the table `second_table` exists, the script shouldn't fail
-- usage of `SELECT` or `SHOW` statements is not allowed

-- Create the table second_table
CREATE TABLE second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

-- Insert records into the table
INSERT INTO second_table(id, name, score) VALUES(1, "John", 10);
INSERT INTO second_table(id, name, score) VALUES(2, "Alex", 3);
INSERT INTO second_table(id, name, score) VALUES(3, "Bob", 14);
INSERT INTO second_table(id, name, score) VALUES(4, "George", 8);
