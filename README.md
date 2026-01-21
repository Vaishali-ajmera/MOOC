# MOOC Platform

A Django-based Massive Open Online Course platform.

## Setup Instructions

### Prerequisites
- Python 3.10+
- PostgreSQL 14+

### Database Setup

```bash
sudo -u postgres psql
CREATE DATABASE mooc_db;
CREATE USER mooc_user WITH PASSWORD 'mooc_pass';
ALTER ROLE mooc_user SET client_encoding TO 'utf8';
ALTER ROLE mooc_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE mooc_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE mooc_db TO mooc_user;
\q
```

### Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Access

- Application: http://localhost:8000
- Admin Panel: http://localhost:8000/admin

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
