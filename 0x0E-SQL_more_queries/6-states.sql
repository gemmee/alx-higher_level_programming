-- creates the db `hbtn_0d_usa` and the table `states`(in the db).
-- the fields of `states`:
-- 	id INT unique, auto generated, can't be null and is a primary key,
-- 	name VARCHAR(256) can't be null
-- the script should not fail if the db or the table already exists.
-- +---------------------+
-- | Author: Gamachu     |
-- | Place: occ, Kaliti  |
-- +---------------------+

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
