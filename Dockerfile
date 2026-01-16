FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Configuration pour la base de données (persistence)
ENV APP_DB_PATH=/data/app.db

# Création du dossier pour le volume
RUN mkdir -p /data

EXPOSE 8000

CMD ["python", "api.py"]
