
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

        
        
