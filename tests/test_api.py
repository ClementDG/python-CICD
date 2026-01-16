import pytest
import os
import sys

# Ajouter le dossier parent au path pour importer les modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api import create_app
import db

@pytest.fixture
def client():
    # Configuration d'une BDD de test
    test_db = "test_app.db"
    os.environ["APP_DB_PATH"] = test_db
    
    # Initialisation de la BDD
    db.init_db()
    
    app = create_app()
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        yield client
        
    # Nettoyage
    if os.path.exists(test_db):
        os.remove(test_db)

def test_health(client):
    """Test que l'endpoint /health répond correctement"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}

def test_create_user(client):
    """Test de création d'un utilisateur"""
    response = client.post("/users", json={"name": "TestUser"})
    assert response.status_code == 201
    assert "id" in response.json

def test_get_user(client):
    """Test de récupération d'un utilisateur"""
    # Créer d'abord un user
    post_resp = client.post("/users", json={"name": "Bob"})
    user_id = post_resp.json["id"]
    
    # Lire le user
    get_resp = client.get(f"/users/{user_id}")
    assert get_resp.status_code == 200
    assert get_resp.json["name"] == "Bob"
