import psycopg2  # On importe psycopg2, une bibliothèque pour se connecter à PostgreSQL
from flask import Flask, request, jsonify  # On importe Flask, request pour lire les requêtes et jsonify pour renvoyer du JSON

app = Flask(__name__)  # On crée une application Flask en lui donnant le nom du module courant

# Variables de configuration pour se connecter à PostgreSQL directement dans le code
DB_HOST = "localhost"   
DB_NAME = "housing_db"  
DB_USER = "matheo"      
DB_PASSWORD = "u6x5qhup"
DB_PORT = "5432"        

def get_connection():
    """
    Cette fonction ouvre une connexion à la base PostgreSQL 
    en utilisant les informations ci-dessus.
    """
    return psycopg2.connect(
        dbname=DB_NAME,        
        user=DB_USER,          
        password=DB_PASSWORD,  
        host=DB_HOST,          
        port=DB_PORT           
    )

@app.route("/houses", methods=["GET"])
def get_houses():
    """
    Quand on fait un GET sur /houses :
    - On se connecte à la base
    - On récupère toutes les lignes de la table 'houses'
    - On renvoie le résultat en JSON
    """
    conn = get_connection()  # On ouvre la connexion à PostgreSQL
    cur = conn.cursor()      # On crée un curseur pour exécuter les requêtes SQL
    cur.execute("""SELECT
        id, longitude, latitude, housing_median_age, total_rooms,
        total_bedrooms, population, households, median_income,
        median_house_value, ocean_proximity
        FROM houses
    """)                     # On récupère toutes les colonnes nécessaires de la table houses
    rows = cur.fetchall()    # On récupère toutes les lignes renvoyées par la requête
    cur.close()              # On ferme le curseur
    conn.close()             # On ferme la connexion à la base

    results = []             # On prépare une liste pour stocker les résultats
    for row in rows:         # Pour chaque ligne récupérée (row)...
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
    # results est maintenant une liste de dictionnaires, plus facile à renvoyer en JSON
    return jsonify(results), 200  # On renvoie la liste en JSON 

@app.route("/houses", methods=["POST"])
def create_house():
    """
    Quand on fait un POST sur /houses :
    - On attend un JSON contenant les infos d'une maison
    - On insère ces infos dans la table 'houses'
    - On renvoie un message de succès
    """
    data = request.get_json()  # On récupère les données JSON envoyées dans la requête

    # Liste des champs obligatoires pour créer une maison
    required_keys = [
        "longitude", "latitude", "housing_median_age",
        "total_rooms", "total_bedrooms", "population",
        "households", "median_income", "median_house_value",
        "ocean_proximity"
    ]
    for key in required_keys:
        # Si un champ manque dans le JSON, on renvoie une erreur 400
        if key not in data:
            return jsonify({"error": f"Missing field '{key}'"}), 400

    try:
        conn = get_connection()  # On se connecte à la base
        cur = conn.cursor()      # On crée un curseur
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
        # On exécute la requête d'insertion avec les valeurs reçues dans data
        cur.execute(query, (
            data["longitude"],
            data["latitude"],
            data["housing_median_age"],
            data["total_rooms"],
            data["total_bedrooms"],
            data["population"],
            data["households"],
            data["median_income"],
            data["median_house_value"],
            data["ocean_proximity"]
        ))
        new_id = cur.fetchone()[0]  
        conn.commit()               
        cur.close()                 
        conn.close()                

        # On renvoie l'id nouvellement créé et un message de succès
        return jsonify({"id": new_id, "message": "House created"}), 201

    except Exception as e:
        # Si jamais on a une erreur quelconque (par exemple de connexion), 
        # on la renvoie dans un JSON avec un code 500 (erreur serveur)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # On lance l'application Flask en mode debug, sur le port 5000
    app.run(debug=True, port=5000)
