## Social Media System

### Components
This repository is divided into 4 components. Reading about each one will help you understand how the system works as a whole.

#### Back-end
The `backend` directory contains an API written in Python using the FastAPI framework. It provides routes for user authentication and the CREATE, READ, UPDATE, and DELETE operations for posts.

The back-end uses JWT for user authentication and always checks for permissions before performing any action.

#### Front-end
The `front-end` directory houses a React.js app, which interacts with the back-end to perform user authentication and post CRUD operations.

#### Infrastructure
The `infrastructure` directory contains the database implementation for this system. It stores user credentials and post data.

This system uses MariaDB, a community-driven fork of MySQL. Fundamentally, they are the same.

#### Scripts
This system uses bcrypt hashes to store passwords in the database. Since the system does not have a sign-up functionality, the script `create-user.py` is used to create a new user in the database, if needed.

Example:
```sh
$ python3 create-user.py turing 1234

Your credentials:
Username: turing, password: 1234

Insert query:
INSERT INTO users (name, password) VALUES ("turing", "$2b$12$rCjKyN0WWvNilO7T5/i5r.8SGunivFlPH1L28WIP6OXkAiqpkH01a");
```

### Running the System
This system uses Docker and Docker Compose to run the application. To get everything up and running, a single command is enough:

```sh
# Run this command from the project's root:
sudo docker compose up
``` 

This command will build the back-end and front-end, pull MariaDB from Docker Hub, launch it, and run the `.sql` file that creates the database and inserts some user credentials.

### After Running
Once the Docker command completes and the services become available, go to http://localhost:8080 to view the login page.

#### Credentials
To make things easier, the Docker Compose setup already injects some users into the system. You can use them to explore the application:
```txt
Username: turing, password: 1234
Username: lovelace, password: abcde
Username: kathleen, password: qwer
```
