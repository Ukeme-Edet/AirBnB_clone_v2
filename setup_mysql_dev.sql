-- Prepares a MySQL database for development purposes.
-- This script is intended to be run on a fresh MySQL installation.
-- Create a new database
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

-- Add a new user
CREATE USER IF NOT EXISTS 'hbnb_dev' @'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges to the new user
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev' @'localhost';

-- Grant SELECT privileges to the new user
GRANT
SELECT
	ON `performance_schema`.* TO 'hbnb_dev' @'localhost';

-- Flush privileges
FLUSH PRIVILEGES;