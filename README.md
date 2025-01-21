<<<<<<< HEAD
## HOUSING-API
=======

# HOUSING-API
>>>>>>> origin/main

## Description

Housing-API is a Flask application connected to a PostgreSQL database. It provides the following endpoints:

<<<<<<< HEAD
GET /houses: retrieve all houses as JSON
POST /houses: add a new house
It manages data such as longitude, latitude, median house age, and more.

## Table of Contents:

Prerequisites
Installation and Setup
Database & Migrations
Running the Application
API Endpoints
Example Requests
Contributors


## Prerequisites:

Python 3.x (ideally 3.10 or higher)
PostgreSQL installed and running
pyenv or pyenv-win if you want to manage multiple Python versions
Alembic for database migrations


## Installation and Setup:

# Clone or download this repository:

bash
[git clone https://github.com/MatheoROUVI/housing-api.git](https://github.com/MathRovi/housing-Matheo-Rouviere.git)
cd housing-api

# Select your Python version using pyenv: Bash

pyenv local 3.10.10 (In my case)

# Create and activate a virtual environment: Bash

# Create a venv:

python -m venv venv

# Windows:

venv\Scripts\activate

# Install dependencies: Bash

pip install -r requirements.txt


## Database Setup:

1. Create the PostgreSQL database:

- Open a terminal/console where you can run psql, and connect as a PostgreSQL superuser: Bash

psql -U postgres

- Create a database (e.g., housing_db) and a user (e.g., matheo) with password: SQL

CREATE DATABASE housing_db;
CREATE USER matheo WITH PASSWORD 'u6x5qhup';
GRANT ALL PRIVILEGES ON DATABASE housing_db TO matheo;

- (Optional) Grant permissions on the public schema if needed: SQL

\c housing_db;
GRANT CREATE ON SCHEMA public TO matheo;


2. Configure Alembic:

- Open the alembic.ini file in the project root.

- Update sqlalchemy.url to match your database. For example: ini

sqlalchemy.url = postgresql://matheo:u6x5qhup@localhost:5432/housing_db

- Run migrations (if a migration is already created): Bash

alembic upgrade head

This will create the houses table in your housing_db database.

## Running the Application

- Ensure your virtual environment is activated: Bash

venv\Scripts\activate

- Start the Flask server: Bash

python app.py

- By default, Flask will run on http://127.0.0.1:5000.

You should see something like:

 * Serving Flask app 'app'
 * Running on http://127.0.0.1:5000/houses 

## API Endpoints

# GET /houses

- Description: Retrieves all houses from the database.

- Response: JSON array of house objects.
Example: Json


=======
- **GET /houses**: Retrieve all houses as JSON.
- **POST /houses**: Add a new house.

The application manages data such as longitude, latitude, median house age, and more.

For the second part of the TP, we implemented Dockerization of the project and database migration using Alembic.

---

## Table of Contents:

1. Prerequisites
2. Installation and Setup
3. Database & Migrations
4. Dockerization
5. Running the Application
6. API Endpoints
7. Example Requests
8. Contributors

---

## Prerequisites:

- Python 3.x (ideally 3.10 or higher)
- PostgreSQL installed and running
- Docker and Docker Compose installed
- Alembic for database migrations

---

## Installation and Setup:

### Clone the repository:

```bash
git clone https://github.com/MathRovi/housing-Matheo-Rouviere.git
cd housing-api
```

### Set up your Python environment:

```bash
# Select your Python version using pyenv:
pyenv local 3.10.10

# Create and activate a virtual environment:
python -m venv venv

# Activate the virtual environment:
venv\Scripts\activate

# Install dependencies:
pip install -r requirements.txt
```

---

## Database Setup:

### 1. Configure PostgreSQL:

- Open PostgreSQL using `psql -U postgres`.
- Create a database and user:

```sql
CREATE DATABASE housing_db;
CREATE USER matheo WITH PASSWORD 'u6x5qhup';
GRANT ALL PRIVILEGES ON DATABASE housing_db TO matheo;
\c housing_db;
GRANT CREATE ON SCHEMA public TO matheo;
```

---

## Dockerization:

We Dockerized the application to make deployment seamless. The `docker-compose.yml` includes two services:
- `api`: The Flask application.
- `db`: The PostgreSQL database.

### Build and run the containers:

```bash
docker-compose up --build
```

### Apply Alembic migrations:

```bash
docker exec -it housing-api-api-1 alembic upgrade head
```

This creates the required `houses` table in the PostgreSQL database.

---

## Running the Application

1. Start the Flask application:
   - Flask runs automatically in the `api` Docker container.

2. Access the API:
   - The API is served on `http://127.0.0.1:5000`.

---

## API Endpoints

### GET /houses

- **Description**: Retrieves all houses from the database.
- **Response**: JSON array of house objects.

Example:

```json
>>>>>>> origin/main
[
  {
    "id": 1,
    "longitude": -122.23,
    "latitude": 37.88,
    "housing_median_age": 41,
    "total_rooms": 880,
    "total_bedrooms": 129,
    "population": 322,
    "households": 126,
    "median_income": 8.3252,
    "median_house_value": 452600,
    "ocean_proximity": "NEAR BAY"
  }
]
<<<<<<< HEAD


# POST /houses

- Description: Inserts a new house record into the database.
- Request Body (JSON):


=======
```

---

### POST /houses

- **Description**: Inserts a new house record into the database.
- **Request Body**:

```json
>>>>>>> origin/main
{
  "longitude": -122.23,
  "latitude": 37.88,
  "housing_median_age": 41,
  "total_rooms": 880,
  "total_bedrooms": 129,
  "population": 322,
  "households": 126,
  "median_income": 8.3252,
  "median_house_value": 452600,
  "ocean_proximity": "NEAR BAY"
}
<<<<<<< HEAD

- Response: JSON


=======
```

- **Response**:

```json
>>>>>>> origin/main
{
  "id": 1,
  "message": "House created"
}
<<<<<<< HEAD


## Example Requests

# Using curl

1. GET all houses: Bash


curl http://127.0.0.1:5000/houses

2. POST a new house: Bash


curl -X POST -H "Content-Type: application/json" \
     -d '{
           "longitude": -122.23,
           "latitude": 37.88,
           "housing_median_age": 41,
           "total_rooms": 880,
           "total_bedrooms": 129,
           "population": 322,
           "households": 126,
           "median_income": 8.3252,
           "median_house_value": 452600,
           "ocean_proximity": "NEAR BAY"
         }' \
     http://127.0.0.1:5000/houses

## Contributors
Name – Matheo R.

## Notes
- Feel free to extend the API with more endpoints (PUT, DELETE, etc.).
- You can also set up more robust environment variable handling (e.g., .env files with python-dotenv) if you prefer.
- This project is provided as an educational or starter example.
=======
```

---

## Example Requests

### Using curl:

#### GET all houses:

```bash
curl http://127.0.0.1:5000/houses
```

#### POST a new house:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"longitude": -122.23, "latitude": 37.88, "housing_median_age": 41, "total_rooms": 880, "total_bedrooms": 129, "population": 322, "households": 126, "median_income": 8.3252, "median_house_value": 452600, "ocean_proximity": "NEAR BAY"}' http://127.0.0.1:5000/houses
```

---

## Contributors
Name: Matheo R.

---

## Notes:
- Extend the API with more endpoints (PUT, DELETE) as needed.
- Use `.env` for secure and scalable environment variable handling.
- This project was developed for educational purposes.
>>>>>>> origin/main
