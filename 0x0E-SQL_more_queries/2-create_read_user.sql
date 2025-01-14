-- creates the db `hbtn_0d_2` and the user `user_0d_2`
-- the user should have only SELECT privilege in the db `hbtn_0d_2` and
-- its password should be set to `user_0d_2_pwd`
-- the script should not fail if the db or the user exists
-- Author: Gamachu
-- Place: occ, Kaliti

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
