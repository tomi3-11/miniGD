
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





