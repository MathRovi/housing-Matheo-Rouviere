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

# Select your Python version using pyenv:

bash
pyenv local 3.10.10 (In my case)

# Create and activate a virtual environment: In bash

# Create a venv:

python -m venv venv

# Windows:

venv\Scripts\activate

# Install dependencies:

bash
pip install -r requirements.txt


## Database connection settings:

You can configure environment variables such as DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, and DB_PORT, or
Hardcode them directly in app.py or a separate config file.
Make sure these point to your PostgreSQL server.
Database & Migrations
Creating the Database Manually
Open PostgreSQL in a terminal (e.g., psql -U postgres).
Create the database (if it doesn’t exist):
sql
Copier
CREATE DATABASE housing_db;
Create a user (if needed) and grant privileges:
sql
Copier
CREATE USER matheo WITH PASSWORD 'u6x5qhup';
GRANT ALL PRIVILEGES ON DATABASE housing_db TO matheo;
(Optional) Grant permissions on the public schema if necessary:
sql
Copier
\c housing_db
GRANT CREATE ON SCHEMA public TO matheo;
Using Alembic Migrations
Edit alembic.ini and set the sqlalchemy.url to connect to your DB. For example:
ini
Copier
sqlalchemy.url = postgresql://matheo:u6x5qhup@localhost:5432/housing_db
Create a migration:
bash
Copier
alembic revision -m "create houses table"
In the generated file (e.g., xxxx_create_houses_table.py), add the op.create_table call:
python
Copier
def upgrade():
    op.create_table(
        'houses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('longitude', sa.Float),
        sa.Column('latitude', sa.Float),
        sa.Column('housing_median_age', sa.Integer),
        sa.Column('total_rooms', sa.Integer),
        sa.Column('total_bedrooms', sa.Integer),
        sa.Column('population', sa.Integer),
        sa.Column('households', sa.Integer),
        sa.Column('median_income', sa.Float),
        sa.Column('median_house_value', sa.Float),
        sa.Column('ocean_proximity', sa.String(50))
    )
Apply the migration:
bash
Copier
alembic upgrade head
If successful, the houses table will be created in your PostgreSQL database.
Running the Application
Activate the virtual environment (if not already):
bash
Copier
venv\Scripts\activate
Run the Flask app:
bash
Copier
python app.py
The server starts on http://127.0.0.1:5000 (by default).
API Endpoints
GET /houses
Description: Fetch all houses from the database in JSON format.
Response:
A JSON array of objects. Each object contains:
id, longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income, median_house_value, ocean_proximity.
Example response (if there is data):

json
Copier
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
    "median_house_value": 452600.0,
    "ocean_proximity": "NEAR BAY"
  }
]
POST /houses
Description: Insert a new house into the database.
Request Body: JSON with the following fields:
json
Copier
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
Response: A JSON object containing an id and a success message. For example:
json
Copier
{
  "id": 1,
  "message": "House created"
}
Example Requests
Using cURL
GET /houses
bash
Copier
curl http://127.0.0.1:5000/houses
POST /houses
bash
Copier
curl -X POST \
     -H "Content-Type: application/json" \
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
Using Postman or Insomnia
GET /houses:

Method: GET
URL: http://127.0.0.1:5000/houses
POST /houses:

Method: POST
URL: http://127.0.0.1:5000/houses
Headers: Content-Type: application/json
Body (raw JSON):
json
Copier
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
Contributors
Your Name – Project setup & code
