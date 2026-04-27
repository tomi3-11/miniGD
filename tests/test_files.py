import io

def test_upload(client, auth):
    # Register
    auth.register()
    # Login and get headers
    headers = auth.get_access_token()

    data = {
        "file": (io.BytesIO(b"Hello world"), "test.txt")
    }

    response = client.post(
        "/api/files/upload", 
        headers=headers,
        data=data,
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
