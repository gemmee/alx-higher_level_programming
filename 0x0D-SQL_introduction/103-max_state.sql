-- imports in hbtn_0c_0 db the `temperatures.sql` table dump
-- temperatures.sql is downloaded in the same folder as this script
-- displays the max temp of each state (ordered by state name)

-- USE hbtn_0c_0;
-- SOURCE ./temperatures.sql;
SELECT state, MAX(value) AS max_temp
	FROM temperatures
	GROUP BY state
	ORDER BY state;
