-- Prepares a MySQL database for testing purposes.
-- This script is intended to be run on a fresh MySQL installation.
-- Create a new database
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- Add a new user
CREATE USER IF NOT EXISTS 'hbnb_test' @'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges to the new user
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test' @'localhost';

-- Grant SELECT privileges to the new user
GRANT
SELECT
	ON `performance_schema`.* TO 'hbnb_test' @'localhost';

-- Flush privileges
FLUSH PRIVILEGES;
