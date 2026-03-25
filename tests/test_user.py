from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

# Существующие пользователи
users = [
    {
        'id': 1,
        'name': 'Ivan Ivanov',
        'email': 'i.i.ivanov@mail.com',
    },
    {
        'id': 2,
        'name': 'Petr Petrov',
        'email': 'p.p.petrov@mail.com',
    }
]


def test_get_existed_user(self):
    response = client.get("/api/v1/user", params={"email": users[0]["email"]})
    assert response.status_code == 200
    assert response.json() == users[0]


def test_get_unexisted_user(self):
    response = client.get("/api/v1/user", params={"email": "unknown@mail.com"})
    assert response.status_code == 404

def test_create_user_with_valid_email(self):
    new_user = {
        "id": 3,
        "name": "Test User",
        "email": "test.user@mail.com",
    }
    response = client.post("/api/v1/user", json=new_user)
    assert response.status_code == 200
    assert response.json() == new_user


def test_create_user_with_invalid_email(self):
    duplicated_user = {
        "id": 4,
        "name": "Duplicate User",
        "email": users[0]["email"],
    }
    response = client.post("/api/v1/user", json=duplicated_user)
    assert response.status_code == 400


def test_delete_user(self):
    user_to_delete = {
        "id": 5,
        "name": "Delete Me",
        "email": "delete.me@mail.com",
    }

    create_response = client.post("/api/v1/user", json=user_to_delete)
    assert create_response.status_code == 200

    delete_response = client.delete(
        "/api/v1/user", params={"email": user_to_delete["email"]}
    )
    assert delete_response.status_code == 200

    get_response = client.get(
        "/api/v1/user", params={"email": user_to_delete["email"]}
    )
    assert get_response.status_code == 404