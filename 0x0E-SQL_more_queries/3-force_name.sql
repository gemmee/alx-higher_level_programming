-- creates the table `force_name` on the MySQL server.
-- the fields of `force_name`: id INT, name VARCHAR(256) can't be null
-- the db name is passed as an arg of the mysql command.
-- the script should not fail if the table already exists.
-- +---------------------+
-- | Author: Gamachu     |
-- | Place: occ, Kaliti  |
-- +---------------------+

CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
