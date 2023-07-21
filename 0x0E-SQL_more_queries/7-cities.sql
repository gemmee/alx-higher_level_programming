-- Creates the db 'hbtn_0d_usa'
-- If the db already exists, the script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Creates a table 'cities' in db 'hbtn_0d_usa' with fields:
-- id INT unique, auto generated, can't be null and is a PK
-- state_id INT, can't be null and must be a FK that references the PK of
-- states table
-- name VARCHAR(256) can't be null
-- If the table already exists, the script should not fail
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);
