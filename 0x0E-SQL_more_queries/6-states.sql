-- Script creates database and a table with a specific description
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states IN hbtn_0d_usa (id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);
