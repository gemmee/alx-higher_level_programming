-- creates the MySQL server user `user_0d_1` with all privileges
-- the user's password should be set to `user_0d_1_pwd`
-- the script shouldn't fail even if the user exists

CREATE USER IF NOT EXISTS `user_0d_1`@`localhost` IDENTIFIED BY 
'user_0d_1_pwd';

GRANT ALL ON *.* TO `user_0d_1`@`localhost`;
