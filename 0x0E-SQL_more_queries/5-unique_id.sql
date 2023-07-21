-- Creates a table 'unique_id' with fields:
-- id INT with the default value 1 and must be unique
-- name VARCHAR(256)
-- If the table exists, the script should not fail
CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
);
