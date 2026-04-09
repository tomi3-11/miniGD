
class AuthAction:
    def __init__(self, client):
        self.client = client

    def register(self, username="testuser", email="test@example.com", password="password123", confirm_password="password123"):
        return self.client.post("/api/auth/register", json={
            "username": username,
            "email": email,
            "password": password,
            "confirm_password": confirm_password
        })

    def login(self, email="test@example.com", password="password123"):
        return self.client.post("/api/auth/login", json={
            "email": email,
            "password": password
        })

        
    def get_access_token(self):
        res = self.login()
        access_token = res.get_json()[0]["tokens"]["access"]
        return {"Authorization": f"Bearer {access_token}"}


    def get_refresh_token(self):
        res = self.login()
        refresh_token = res.get_json()[0]["tokens"]["refresh"]
        return {"Authorization": f"Bearer {refresh_token}"}
        
