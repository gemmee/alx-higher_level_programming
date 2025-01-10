-- Converts `hbtn_0c_0` db to UTF8(utf8mb4, collate utf8mb4_unicode_ci)
-- Things need to be converted:
-- 	database `hbtn_0c_0`
-- 	table `first_table`
-- 	field `name` in first_table
-- Author: Gamachu
-- Place: occ, Kaliti

ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE `first_table`
	CHANGE COLUMN `name` `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
