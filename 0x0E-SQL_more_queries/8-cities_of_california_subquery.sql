-- lists all the cities of California that are in db `hbtn_0d_usa`
-- the states table contains only one record where name = California
-- results must be sorted in ascending order by cities.id
-- usage of the JOIN keyword is not allowed
-- the db name is passed as an arg of the mysql command.

-- +---------------------+
-- | Author: Gamachu     |
-- | Place: occ, Kaliti  |
-- +---------------------+

-- query using subquery
SELECT id, name
	FROM cities
	WHERE state_id = (SELECT id FROM states WHERE name = 'California')
	ORDER BY id;
