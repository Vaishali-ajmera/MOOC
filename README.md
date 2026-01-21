# MOOC Platform

A Django-based Massive Open Online Course platform with Docker support.

## Quick Start with Docker

### 1. Setup Environment

```bash
cp .env.example .env
```

Update `.env` with your values.

### 2. Build and Run

```bash
docker-compose up --build
```

### 3. Create Superuser

```bash
docker-compose exec web python manage.py createsuperuser
```

### 4. Access

- **Application**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin

## Environment Variables

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | Debug mode |
| `DB_NAME` | Database name |
| `DB_USER` | Database user |
| `DB_PASSWORD` | Database password |
| `DB_HOST` | Database host |
| `DB_PORT` | Database port |

## Project Structure

```
mooc/
├── config/          # Project settings
├── courses/         # Course and Lesson models
├── enrollments/     # Enrollment and progress tracking
├── accounts/        # User authentication
└── templates/       # HTML templates
```

## Features

- User authentication (signup, login, logout)
- Course catalog with list and detail views
- Enrollment system
- Lesson tracking with progress indicators
- My Courses page for enrolled courses
