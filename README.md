# JWT Authentication API

A simple authentication API built with Django, Django REST Framework (DRF), Simple JWT, and Swagger/OpenAPI documentation.

The API allows users to:

- Register a new account
- Authenticate and obtain JWT tokens
- Access a protected profile endpoint using a valid JWT
- Features
- User registration with secure password hashing
- JWT-based authentication using Simple JWT
- Protected profile endpoint
- Input validation using DRF serializers
- Interactive API documentation with Swagger
- Custom User model support
- SQLite database for persistence


## Tech Stack


| Component         | Technology                          |
|-------------------|-------------------------------------|
| Backend           | Django 6                            |
| Database          | Sqlite                              |
| Authentication    | Django REST Framework + SimpleJWT   |
| Package management| uv                |  
| CORS              | django-cors-headers                 |


## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/agigibairene/minoHealth_assignment.git
cd authentication
```

### 2. Create a Virtual Environment

Using uv:

```bash
uv venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
uv sync
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

## API Endpoints

### Register

Creates a new user account.

**Endpoint**

```http
POST /register/
```

**Request Body**

```json
{
  "username": "irene",
  "password": "StrongPassword123!"
}
```

**Response**

```json
{
  "message": "User registered successfully"
}
```

---

### Login

Authenticates a user and returns JWT tokens.

**Endpoint**

```http
POST /login/
```

**Request Body**

```json
{
  "username": "irene",
  "password": "StrongPassword123!"
}
```

**Response**

```json
{
  "refresh": "refresh_token",
  "access": "access_token"
}
```

---

### Profile

Returns information about the currently authenticated user.

**Endpoint**

```http
GET /profile/
```

**Headers**

```http
Authorization: Bearer <access_token>
```

**Response**

```json
{
  "id": 1,
  "username": "irene"
}
```

---

## Authentication Flow

1. Register a new user via `/register/`
2. Login via `/login/`
3. Receive access and refresh tokens
4. Include the access token in the Authorization header
5. Access protected endpoints such as `/profile/`

Example:

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```


## JWT Configuration

Access token lifetime:

```text
60 minutes
```

Refresh token lifetime:

```text
3 days
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/schema/swagger-ui/
```

OpenAPI Schema:

```text
http://127.0.0.1:8000/schema/
```


## Project Structure

```text
authentication/
├── auth_app/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── authentication/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── pyproject.toml
├── uv.lock
├── README.md
└── db.sqlite3
```


## Security

- Passwords are hashed using Django's built-in password hashing system.
- JWT tokens are signed and verified using Simple JWT.
- Protected routes require valid authentication tokens.
- Access tokens have a limited lifespan to reduce security risks.
