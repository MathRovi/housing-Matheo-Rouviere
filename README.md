## HOUSING-API

## Description

Housing-API is a Flask application connected to a PostgreSQL database. It provides the following endpoints:

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
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

## API Endpoints

# GET /houses

- Description: Retrieves all houses from the database.

- Response: JSON array of house objects.
Example: Json


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


# POST /houses

- Description: Inserts a new house record into the database.
- Request Body (JSON):


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

- Response: JSON


{
  "id": 1,
  "message": "House created"
}


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
Your Name – Matheo R.

## Notes
- Feel free to extend the API with more endpoints (PUT, DELETE, etc.).
- You can also set up more robust environment variable handling (e.g., .env files with python-dotenv) if you prefer.
- This project is provided as an educational or starter example.
