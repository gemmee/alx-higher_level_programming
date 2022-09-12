-- displays the number of records with id = 89 in the table first_table
-- of the database hbtn_0c_0 in my local MySQL server
-- The database name will be passed as an argument of mysql command

-- SELECT COUNT(*) FROM first_name WHERE id = 89; 
SELECT COUNT(id) FROM first_table WHERE id=89; 
