from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os

# Crée l'application Flask
app = Flask(__name__)

# Configuration de la connexion à la base de données PostgreSQL
# Assurez-vous que le mot de passe correspond à celui défini dans docker-compose.yml
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://matheo:u6x5qhup@db:5432/housing_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation de SQLAlchemy pour gérer la base de données
db = SQLAlchemy(app)

# Modèle pour la table "houses"
class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    housing_median_age = db.Column(db.Integer, nullable=False)
    total_rooms = db.Column(db.Integer, nullable=False)
    total_bedrooms = db.Column(db.Integer, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    households = db.Column(db.Integer, nullable=False)
    median_income = db.Column(db.Float, nullable=False)
    median_house_value = db.Column(db.Float, nullable=False)
    ocean_proximity = db.Column(db.String(50), nullable=False)

# Route GET pour obtenir toutes les maisons
@app.route('/houses', methods=['GET'])
def get_houses():
    try:
        houses = House.query.all()
        results = []
        for house in houses:
            house_data = {
                'id': house.id,
                'longitude': house.longitude,
                'latitude': house.latitude,
                'housing_median_age': house.housing_median_age,
                'total_rooms': house.total_rooms,
                'total_bedrooms': house.total_bedrooms,
                'population': house.population,
                'households': house.households,
                'median_income': house.median_income,
                'median_house_value': house.median_house_value,
                'ocean_proximity': house.ocean_proximity
            }
            results.append(house_data)
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route POST pour ajouter une maison
@app.route('/houses', methods=['POST'])
def create_house():
    try:
        data = request.get_json()

        # Validation des champs nécessaires
        required_fields = [
            'longitude', 'latitude', 'housing_median_age',
            'total_rooms', 'total_bedrooms', 'population',
            'households', 'median_income', 'median_house_value', 'ocean_proximity'
        ]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field '{field}'"}), 400

        # Création de la nouvelle maison
        new_house = House(
            longitude=data['longitude'],
            latitude=data['latitude'],
            housing_median_age=data['housing_median_age'],
            total_rooms=data['total_rooms'],
            total_bedrooms=data['total_bedrooms'],
            population=data['population'],
            households=data['households'],
            median_income=data['median_income'],
            median_house_value=data['median_house_value'],
            ocean_proximity=data['ocean_proximity']
        )

        db.session.add(new_house)
        db.session.commit()

        return jsonify({
            "message": "House created successfully",
            "id": new_house.id
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vérifier la connexion à la base de données lors du démarrage
def check_db_connection():
    try:
        connection = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        connection.close()
    except Exception as e:
        print(f"Database connection failed: {str(e)}")
        exit(1)

# Vérification de la connexion avant de démarrer l'application
check_db_connection()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
