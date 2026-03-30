# Authentication Documentation
This is a documentation for the authentication blueprint

## Auth endpoints
Root URL: `http://localhost:5000/api/auth/`

| s/No | Method | Endpoint       | Explanation       |
|------|--------|----------------|-------------------|
| 1    | `GET`  | `/`            | Home url, gives information about the api |
| 2    | `POST` | `/register`    | Accepts some json then creates a user account |
| 3    | `POST` | `/login`       | Accepts some json if correct logs in the user and provide them with tokens |
| 4    | `POST` | `/token/refresh`       | this refreshes the access token provided the refresh token |
| 5    | `POST` | `/me`       | returns user details |
| 6    | `POST` | `/password/reset`       | This request for a new password given an email |
| 7    | `POST` | `/password/reset/confirm`       | This confirms the new password reset |


## `JSON` outputs
Here are the output for the following commands:

### Home Blueprint
1. home url

Endpoint: `/`

command: `curl -X GET http://localhost:5000/`<br>
Output:
```json
[
  {
    "Details": "This is simply an experiment building a mini google drive, the goal is to know how to work with files and object storage locally using minIO",
    "message": "Welcome to my mini Google Drive"
  },
  200
]
```

### Auth Blueprint
All auth blueprint

Root: `http://localhost:5000/api/auth`

1. Registration.

Endpoint: `/register`<br>
Command:
```sh
curl -X POST http://localhost:5000/api/auth/register \ 
     -H 'Content-Type: application/json' \ 
     -d '{username: testuser, email: xmusstores@gmail.com, password: testpassword, confirm_password: testpassword}' | jq

```

Output:
```json
[
  {
    "message": "User registered successfully"
  },
  201
]
```
2. Login.

Endpoint: `/login`<br>
Command:
```sh
curl -X POST http://localhost:5000/api/auth/login \ 
     -H 'Content-Type: application/json' \ 
     -d '{"email": "xmusstores@gmail.com", "password": "testpassword"}' | jq

```

Output:
```json
[
  {
    "tokens": {
      "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVC..."
      "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    },
    "user": {
      "email": "xmusstores@gmail.com",
      "id": "38e151da...",
      "username": "testuser"
    }
  },
  200
]
```
3. User profile.

Endpoint: `/me`<br>
Command:
```sh
curl -X GET http://localhost:5000/api/auth/me \ 
     -H 'Authorization: Bearer <Access Token>' \ 

```

Output:
```json
[
  {
    "email": "xmusstores@gmail.com",
    "id": "38e151da...",
    "username": "testuser"
  },
  200
]
```
4. Refresh token.

Endpoint: `/token/refresh`<br>
Command:
```sh
curl -X POST http://localhost:5000/api/auth/token/refresh \ 
     -H 'Authorization: Bearer <Refresh Token>'  

```

Output:
```json
[
  {
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc3NDg5NjIwNiwianRpIjoiMDdjNTJkZGYtNTA3ZS00NDc2LWI0NjUtMTE5YTQzNDllYWUyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjM4ZTE1MWRhLWU3MDktNDBlNi04YmYyLWJkMWU4Yjg1NGZkMiIsIm5iZiI6MTc3NDg5NjIwNiwiY3NyZiI6ImQ2OGM0NTA0LTMzODktNDgyMi1iNjUxLTRjNjEyMGM0NDZhYyIsImV4cCI6MTc3NDg5OTgwNn0.Gmaw5XhVX5bupMIKbYeELHn9tgsn4vfySZHQM0D08jo"
  },
  200
]
```
