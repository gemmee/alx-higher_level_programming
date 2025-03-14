-- imports in hbtn_0c_0 db `temperatures.sql` table dump which
-- is downloaded in the same folder as this script
-- displays the top 3 of cities temp during Jul.(7) and Aug.(8)
-- ordered by temp (desc)

-- USE hbtn_0c_0;
-- SOURCE ./temperatures.sql;
SELECT city, AVG(value) AS avg_temp
	FROM temperatures
	WHERE month = 7 OR month = 8
	GROUP BY city
	ORDER BY avg_temp DESC
	LIMIT 3;
