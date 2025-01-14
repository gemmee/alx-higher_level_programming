-- creates the db `hbtn_0d_usa` and the table `cities`(in the db).
-- the fields of `cities`:
-- 	id INT unique, auto generated, can't be null and is a primary key,
-- 	state_id INT, can't be null and must be a FOREIGN KEY that references to id of the states table
-- 	name VARCHAR(256) can't be null
-- the script should not fail if the db or the table already exists.
-- +---------------------+
-- | Author: Gamachu     |
-- | Place: occ, Kaliti  |
-- +---------------------+

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT PRIMARY KEY, -- implicitly NOT NULL and UNIQUE
	name VARCHAR(256) NOT NULL,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
