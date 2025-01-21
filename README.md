
# HOUSING-API

## Description

Housing-API is a Flask application connected to a PostgreSQL database. It provides the following endpoints:

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
```

---

### POST /houses

- **Description**: Inserts a new house record into the database.
- **Request Body**:

```json
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
```

- **Response**:

```json
{
  "id": 1,
  "message": "House created"
}
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
