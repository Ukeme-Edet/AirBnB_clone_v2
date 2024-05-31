-- This script is used to setup the MySQL database for the development environment.
-- It creates the database, the user, and the tables.
-- Create the database
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

-- Create the user
CREATE USER IF NOT EXISTS 'hbnb_dev' @'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges to the user
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev' @'localhost';

-- Grant privileges to the user
GRANT ALL PRIVILEGES ON `performance_schema`.* TO 'hbnb_dev' @'localhost';
