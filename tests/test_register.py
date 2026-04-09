
def test_register_user(client):
    response = client.post("/api/auth/register", json={
        "username": "user",
        "email": "user@example.com",
        "password": "password123",
        "confirm_password": "password123"
    })

    assert response.status_code == 200
    assert response.get_json()[0]["message"] == "User registered successfully"
