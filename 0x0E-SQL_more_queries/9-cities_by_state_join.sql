-- Lists all cities contained in the db hbtn_0d_usa
-- Each record should display cities.id, cities.name, states.name
-- Sort the result by cities.id in ascending order
-- You can use only one SELECT statement
SELECT c.id, c.name, s.name FROM cities AS c LEFT JOIN states AS s
ON c.state_id = s.id ORDER BY c.id;
