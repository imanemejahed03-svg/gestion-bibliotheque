
# 1. Image de base Python
FROM python:3.13-slim

# 2. Définir le répertoire de travail
WORKDIR /app

# 3. Copier les dépendances
COPY requirements.txt .

# 4. Installer les bibliothèques Python
RUN pip install --no-cache-dir --timeout 120 --retries 10 -r requirements.txt

# 5. Copier le reste du projet
COPY . .

# 6. Exposer le port Flask
EXPOSE 5000

# 7. Démarrer l'application
CMD ["python", "app.py"]
