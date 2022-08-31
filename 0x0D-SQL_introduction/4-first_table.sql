-- creates a table called first_table in the current database
-- the database is passed as an argument to mysql command
-- do not use SELECT or SHOW statements
-- does not fail if table exists
CREATE TABLE IF NOT EXISTS first_table(id INT, name VARCHAR(256));
