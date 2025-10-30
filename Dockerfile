# Image de base
FROM python:3.11-slim

# Défini le répertoire de travail
WORKDIR /app

# Copie les fichiers du projet
COPY . /app

# Installe les dépendances
RUN pip install --no-cache-dir fastmcp uvicorn

# Exposer le port du serveur
EXPOSE 8000

# Commande pour lancer le serveur
CMD ["python", "server.py"]
