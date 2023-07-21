-- Creates a table 'id_not_null' with these fields:
-- id INT default value 1, name VARCHAR(256)
-- If table already exists, script should not fail
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);

