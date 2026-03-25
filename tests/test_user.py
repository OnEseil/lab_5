from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

users = [
    {"id": 1, "name": "Ivan Ivanov", "email": "i.i.ivanov@mail.com"},
    {"id": 2, "name": "Petr Petrov", "email": "p.p.petrov@mail.com"},
]


def test_get_existed_user():
    response = client.get("/api/v1/user", params={"email": users[0]["email"]})
    assert response.status_code == 200
    assert response.json() == users[0]

def test_get_unexisted_user():
    response = client.get("/api/v1/user", params={"email": "unknown@mail.com"})
    assert response.status_code == 404


def test_create_user_with_invalid_email():
    duplicated_user = {
        "id": 999,
        "name": "Duplicate User",
        "email": users[0]["email"],
    }
    response = client.post("/api/v1/user", json=duplicated_user)
    assert response.status_code == 409


def test_delete_user():
    response = client.delete("/api/v1/user", params={"email": users[1]["email"]})
    assert response.status_code == 204

    get_response = client.get("/api/v1/user", params={"email": users[1]["email"]})
    assert get_response.status_code == 404