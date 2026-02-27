# Social Media API

## Project Overview
This project is a Social Media API built with Django and Django REST Framework.
It includes custom user authentication with token-based authentication.

## Features
- Custom User Model
- User Registration
- User Login
- Token Authentication
- Profile Management
- Followers System

## Setup Instructions

1. Clone repository
2. Create virtual environment
3. Install dependencies:
   pip install -r requirements.txt
4. Run migrations:
   python manage.py makemigrations
   python manage.py migrate
5. Start server:
   python manage.py runserver

## API Endpoints

POST /api/register/
POST /api/login/
GET/PUT /api/profile/

## Authentication
Uses DRF Token Authentication.
Include header:
Authorization: Token <"366d00983fca3c98e79c23e646027e5c6f61e4ed">