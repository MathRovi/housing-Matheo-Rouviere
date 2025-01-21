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
CMD ["python", "app.py"]
