
def test_register_user(auth):
    response = auth.register()

    assert response.status_code == 200
    assert response.get_json()[0]["message"] == "User registered successfully"



def test_login_success(auth):
    # Register a user first
    auth.register()

    # Login
    response = auth.login()

    assert response.status_code == 200
    assert "access" in response.get_json()[0]["tokens"]


def test_profile(client, auth):
    # Register
    auth.register()
    # get access token
    headers = auth.get_access_token()

    response = client.get("/api/auth/me", headers=headers)

    assert response.status_code == 200
    assert "email" in response.get_json()[0]
    assert "username" in response.get_json()[0]
    assert "id" in response.get_json()[0]


def test_refresh_token(client, auth):
    # Register
    auth.register()
    # Login
    headers = auth.get_refresh_token()

    response = client.post("/api/auth/token/refresh", headers=headers)

    # test
    assert response.status_code == 200
    assert "access" in response.get_json()[0]


def test_logout(client):
    response = client.get("/api/auth/logout")

    assert response.status_code == 200
    assert "message" in response.get_json()[0]


