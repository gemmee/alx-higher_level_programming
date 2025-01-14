-- creates the table `unique_id` on the MySQL server.
-- the fields of `id_not_null`:
-- 	id INT with the default value 1 and must be unique,
-- 	name VARCHAR(256)
-- the db name is passed as an arg of the mysql command.
-- the script should not fail if the table already exists.
-- +---------------------+
-- | Author: Gamachu     |
-- | Place: occ, Kaliti  |
-- +---------------------+

CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
);
