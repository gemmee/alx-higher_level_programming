-- lists all cities contained in the db `hbtn_0d_usa`.
-- each record should display: cities.id - cities.name - states.name
-- usage of more than one SELECT statement is not allowed
-- results must be sorted in ascending order by cities.id
-- the db name is passed as an arg of the mysql command.

-- +---------------------+
-- | Author: Gamachu     |
-- | Place: occ, Kaliti  |
-- +---------------------+

-- query using INNER JOIN
SELECT cities.id, cities.name, states.name
	FROM cities INNER JOIN states
	ON states.id = cities.state_id
	ORDER BY cities.id;

-- equivalent query using comma-separated syntax (less clear)
--SELECT cities.id, cities.name, states.name
--	FROM cities, states  -- implicit cartesian join
--	WHERE states.id = cities.state_id
--	ORDER BY cities.id;

-- equivalent query using CROSS JOIN (less efficient)
--SELECT cities.id, cities.name, states.name
--	FROM cities CROSS JOIN states
--	WHERE states.id = cities.state_id
--	ORDER BY cities.id;

