-- imports in hbtn_0c_0 db a table dump which
-- is downloaded in the same folder as this script with
-- a file name temperatures.sql and then
-- displays the average temperature (Fahrenheit) by city
-- ordered by temperature (descending)

-- select the target database
USE hbtn_0c_0;
-- import the dump file
SOURCE ./temperatures.sql;
-- verify the import
-- SHOW TABLES;
-- SELECT * FROM temperatures LIMIT 10;

-- display the average temp by city ordered by temp(desc)
SELECT city, AVG(value) AS avg_temp FROM temperatures
	GROUP BY city
	ORDER BY avg_temp DESC;
