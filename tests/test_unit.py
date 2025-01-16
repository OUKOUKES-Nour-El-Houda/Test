from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

# Test de la route GET /trainers
def test_get_trainers():
    response = client.get("/trainers")
    assert response.status_code == 200
    trainers = response.json()
    assert trainers[5]['name'] == "Abir"
