# Medical App

A Django app for recording **diseases and their symptoms**, written by doctors, so patients can look up conditions. It includes doctor and patient sign-up and login.

## Features

- List of diseases with symptoms, doctor and date
- Add a disease entry (with an optional image)
- Detail page for each entry
- Sign up, log in and log out

## Running

```bash
cd MedicalAPI
python -m venv venv && source venv/bin/activate
pip install "django<2" pillow       # uses the url() routing from Django 1.x
python manage.py migrate
python manage.py runserver          # http://localhost:8000
```

## Routes

| Path | Description |
|---|---|
| `/` | Home |
| `/diseases/` | Disease list |
| `/diseases/create/` | Add a disease |
| `/diseases/<slug>/` | Disease detail |
| `/patients/signup/`, `/patients/login/` | Accounts |

## Tech

Python · Django 1.x · SQLite · Pillow
