import psycopg2  # Importer la bibliothèque pour se connecter à PostgreSQL
from flask import Flask, request, jsonify  # Importer Flask, request pour lire les données de la requête et jsonify pour renvoyer du JSON

app = Flask(__name__)  # Initialiser l'application Flask

# Variables de connexion à la base de données PostgreSQL
DB_HOST = "db"  # Utiliser "db" car c'est le nom du service de PostgreSQL dans docker-compose.yml
DB_NAME = "housing_db"
DB_USER = "matheo"
DB_PASSWORD = "u6x5qhup"
DB_PORT = "5432"

def get_connection():
    """
    Cette fonction établit la connexion à la base PostgreSQL.
    """
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

@app.route("/", methods=["GET"])
def home():
    """
    Route de la page d'accueil pour afficher un message de bienvenue.
    """
    return jsonify({"message": "Bienvenue sur l'API Housing! Utilisez /houses pour accéder aux données."}), 200

@app.route("/houses", methods=["GET"])
def get_houses():
    """
    Cette route permet de récupérer toutes les maisons dans la base de données.
    """
    conn = get_connection()  # Se connecter à la base de données
    cur = conn.cursor()  # Créer un curseur pour exécuter les requêtes SQL
    cur.execute("""
        SELECT
            id, longitude, latitude, housing_median_age, total_rooms,
            total_bedrooms, population, households, median_income,
            median_house_value, ocean_proximity
        FROM houses
    """)  # Exécuter la requête pour récupérer les maisons
    rows = cur.fetchall()  # Récupérer tous les résultats
    cur.close()  # Fermer le curseur
    conn.close()  # Fermer la connexion à la base

    # Formater les résultats sous forme de JSON
    results = []
    for row in rows:
        results.append({
            "id": row[0],
            "longitude": row[1],
            "latitude": row[2],
            "housing_median_age": row[3],
            "total_rooms": row[4],
            "total_bedrooms": row[5],
            "population": row[6],
            "households": row[7],
            "median_income": row[8],
            "median_house_value": row[9],
            "ocean_proximity": row[10]
        })
    
    return jsonify(results), 200  # Retourner les données sous forme de JSON

@app.route("/houses", methods=["POST"])
def create_house():
    """
    Cette route permet d'ajouter une nouvelle maison dans la base de données.
    """
    data = request.get_json()  # Récupérer les données JSON envoyées dans la requête

    # Liste des champs obligatoires
    required_keys = [
        "longitude", "latitude", "housing_median_age",
        "total_rooms", "total_bedrooms", "population",
        "households", "median_income", "median_house_value",
        "ocean_proximity"
    ]
    
    for key in required_keys:
        if key not in data:  # Si un champ est manquant
            return jsonify({"error": f"Missing field '{key}'"}), 400

    try:
        conn = get_connection()  # Se connecter à la base de données
        cur = conn.cursor()  # Créer un curseur pour exécuter la requête
        query = """
        INSERT INTO houses (
            longitude, latitude, housing_median_age,
            total_rooms, total_bedrooms, population,
            households, median_income, median_house_value,
            ocean_proximity
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
        """
        # Exécuter la requête d'insertion avec les données reçues
        cur.execute(query, (
            data["longitude"], data["latitude"], data["housing_median_age"],
            data["total_rooms"], data["total_bedrooms"], data["population"],
            data["households"], data["median_income"], data["median_house_value"],
            data["ocean_proximity"]
        ))
        new_id = cur.fetchone()[0]  # Récupérer l'ID généré
        conn.commit()  # Confirmer les changements dans la base de données
        cur.close()  # Fermer le curseur
        conn.close()  # Fermer la connexion à la base

        return jsonify({"id": new_id, "message": "House created"}), 201  # Retourner le succès

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # En cas d'erreur, renvoyer un message d'erreur

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # Lancer l'application Flask en mode debug