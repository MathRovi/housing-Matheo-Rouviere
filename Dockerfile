<<<<<<< HEAD
# Utiliser une image Python de base
FROM python:3.10-slim

# Définir un répertoire de travail
WORKDIR /app

# Copier les fichiers de l'API (y compris requirements.txt)
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port (optionnel, juste pour la doc)
EXPOSE 5000

# Démarrer l'application
=======
# Utilisation de l'image Python 3.10
FROM python:3.10-slim

# Créer un répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le reste du code de l'application dans le conteneur
COPY . .

# Exposer le port 5000 que Flask utilise par défaut
EXPOSE 5000

# Commande pour démarrer l'application Flask
>>>>>>> de1c9e4 (Dépot Partie 2 du TP)
CMD ["python", "app.py"]
