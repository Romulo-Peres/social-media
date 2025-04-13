DROP DATABASE IF EXISTS blog;

CREATE DATABASE blog;

USE blog;

CREATE TABLE users(
       id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
       name VARCHAR(256) NOT NULL UNIQUE,
       password VARCHAR(256) NOT NULL
);

CREATE TABLE posts(
       id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
       title VARCHAR(256) NOT NULL,
       content VARCHAR(2048) NOT NULL,
       publisher_id INTEGER NOT NULL,
       FOREIGN KEY(publisher_id) REFERENCES users(id)
);

CREATE USER 'not-root'@'%' IDENTIFIED BY '$1AnIncredibleStrongPassword1$';
GRANT ALL PRIVILEGES ON blog.* TO 'not-root'@'%';

INSERT INTO users (name, password) VALUES ("turing", "$2b$12$Q8K19LhyNnaBYRA4I4MRYuhbwVEYXy8M8OyhXhby0MgMa9fZgFKea");
INSERT INTO users (name, password) VALUES ("lovelace", "$2b$12$9zknxe4NCy0b5F2gFeu9Xe1HWpVn5gDVsxuy5tksYa/areB//T2EK");
INSERT INTO users (name, password) VALUES ("kathleen", "$2b$12$jiDfJOPH3iRyFstnUe2l7eHrm2kDnNPSOdr5vGaxlvSH.vL2nn/Tu");
