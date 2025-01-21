## HOUSING-API

### Description

Housing-API est une application Flask connectée à une base de données PostgreSQL. Elle fournit les endpoints suivants :

- **GET /houses** : Récupère toutes les maisons sous forme de JSON.
- **POST /houses** : Ajoute une nouvelle maison.

Elle gère des données comme la longitude, la latitude, l'âge médian des maisons, et plus encore.

---

### Table des matières

1. Prérequis
2. Installation et configuration
3. Configuration de la base de données et migrations
4. Exécution de l'application
5. Points de terminaison API
6. Exemples de requêtes
7. Contributeurs

---

### Prérequis

- Python 3.x (idéalement 3.10 ou supérieur)
- PostgreSQL installé et en cours d'exécution
- Docker et Docker Compose installés
- Alembic pour les migrations de base de données

---

### Installation et configuration

#### Cloner le dépôt

```bash
git clone https://github.com/MathRovi/housing-Matheo-Rouviere.git
cd housing-api
