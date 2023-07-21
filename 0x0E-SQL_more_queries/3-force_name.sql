-- Create table 'force_name' with fields
-- id INT, name VARCHAR(256) can't be null
-- If table already exists, script should not fail
CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHaR(256) NOT NULL
);
