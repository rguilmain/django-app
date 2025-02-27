# Django Application

[![CI](https://github.com/rguilmain/django-app/actions/workflows/ci.yml/badge.svg)](https://github.com/rguilmain/django-app/actions/workflows/ci.yml)

Cookie cutter Django project.

## Setup

1. Clone the repository
2. Copy `.env.example` to `.env` and update the settings
3. Run `docker-compose up --build`
4. Go to `http://localhost:8000`

## Development

1. Install development dependencies: `pip install -r requirements/dev.txt`
2. Run tests: `pytest`
3. Format code: `black .`
4. Check linting: `flake8`

## Production

For production deployment, set `DEBUG=False` in your .env file and ensure all security settings are properly configured.

## Usage

1. Enter text in the text field
2. Click the submit button
3. See the text you entered in the text field
