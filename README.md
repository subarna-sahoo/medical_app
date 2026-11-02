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

## Configuration

Secrets are read from **environment variables**, so nothing sensitive lives in the code. Copy [`.env.example`](.env.example) to `.env` (it is git-ignored) or export the variables in your shell:

| Variable | Purpose |
|---|---|
| `DJANGO_SECRET_KEY` | Django `SECRET_KEY`. If unset, a random key is generated at startup (fine for local dev). |

The same values are stored as **GitHub Actions secrets** on this repo (*Settings → Secrets and variables → Actions*), so CI/CD workflows can use them as `${{ secrets.NAME }}`.
