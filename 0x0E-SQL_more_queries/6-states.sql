-- Creates a db 'hbtn_0d_usa' and within it a table 'states'
-- The table 'states' have the ff fields:
-- id INT unique, auto generated, can't be null and primary key
-- name VARCHAR(256) can't be null
-- The script should not fail in case either the db or the table exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY(id)
);
