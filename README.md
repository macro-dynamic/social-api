# Social Media API

## Overview

This project is the backend for a Social Media API. The API supports user registration, creating and managing posts, following users, and viewing feeds.

## Features

- **User Management**: Register, login, and manage user profiles.
- **Post Management**: Create, update, delete, and retrieve posts.
- **Follow System**: Follow and unfollow users.
- **Feed**: View a feed of posts from followed users.

## Prerequisites

- Python 3.8+
- Django 4.0+
- Git

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/macro-dynamic/social-media-api.git
cd social-media-api
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

- On Linux/MacOS:
  ```bash
  source venv/bin/activate
  ```
- On Windows:
  ```bash
  venv\Scripts\activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional for Admin Access)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Access the API at `http://127.0.0.1:8000/`.

## Project Structure

```
.
├── social_media_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── app/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── .gitignore
├── README.md
└── requirements.txt
```

## .gitignore

The `.gitignore` file ensures sensitive and unnecessary files are excluded from version control. It includes:

- `venv/`
- `*.pyc`
- `__pycache__/`
- `.DS_Store`

## Deployment

For deployment, you can use services like Heroku, PythonAnywhere, or AWS. Update the `settings.py` file with production configurations, including `ALLOWED_HOSTS` and database settings.




