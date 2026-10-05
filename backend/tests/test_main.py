from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to CI/CD Demo API"}


def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_message():
    response = client.get("/api/message")
    assert response.status_code == 200
    assert response.json()["message"] == "Hello from FastAPI Backend!"
