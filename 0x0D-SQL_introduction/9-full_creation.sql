-- creates a table second_table in the db hbtn_0c_0 in my local
-- MySQL server and adds multiple rows

CREATE TABLE IF NOT EXISTS second_table(
	id INT,
	name VARCHAR(256),
	score INT
);

INSERT INTO second_table(id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table(id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table(id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table(id, name, score) VALUES (4, 'George', 8);

-- you can also insert the values with a single statement like this:
/*
INSERT INTO second_table(id, name, score) VALUES
	(1, 'John', 10), 
	(2, 'Alex', 3), 
	(3, 'Bob', 14), 
	(4, 'George', 8);
*/
