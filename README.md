# Search Bar
## Overview
A simple search bar for searching through a list of user profiles (first name and last name data), created using React, Django, PostgreSQL and Docker.

## Setup
### Prerequisites
Make sure you have installed the following on your machine:
- [Git](https://git-scm.com/downloads)
- [Docker](https://docs.docker.com/engine/install/)

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/yorozuya-2003/SearchBar.git
    ```

2. Run the Docker container using docker-compose in the root directory of the repository:
    ```sh
    docker compose up
    ```

3. Set up the database (changes can be made in PostgreSQL database by modifying the `.env` file in the root directory or through bash shell of postgres container after running the above command):
    - Open a new terminal window and run the following command to view the active containers:
        ```sh
        docker ps
        ```
    - Copy the container ID of the `searchbar_backend` container.
    - Run the following command to access the container's bash shell:
        ```sh
        docker exec -it <container_id> bash
        ```
    - Run the following command to make migrations to the database:
        ```sh
        python manage.py migrate
        ```

4. Access the REST API:
    - Open a web browser and go to http://localhost:8000/api/profiles/ to view the list of user profiles.
    - Make a GET, POST, PUT or DELETE request to interact with the user profile data in the database.

5. Access the frontend:
    - Open a web browser and go to http://localhost:3000/ to view the search bar.

6. To stop the Docker container, use `Ctrl + C` in the terminal window where the container is running.

## Author
[Tanish Pagaria](https://github.com/yorozuya-2003)  
*(IIT Jodhpur Undergraduate)*
