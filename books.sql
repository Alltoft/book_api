-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS books;
GRANT ALL PRIVILEGES ON `books`.* TO 'root'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
