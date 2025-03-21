-- creates the table `id_not_null` on the MySQL server.
-- the fields of `id_not_null`:
-- 	id INT with the default value 1,
-- 	name VARCHAR(256)
-- the db name is passed as an arg of the mysql command.
-- the script should not fail if the table already exists.
-- +---------------------+
-- | Author: Gamachu     |
-- | Place: occ, Kaliti  |
-- +---------------------+

CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);
