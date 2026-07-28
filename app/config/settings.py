"""
Application Settings

This file loads all environment variables from the .env file.

Instead of calling os.getenv() throughout the application,
we centralize configuration in one place.
"""

import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "Production GitOps API")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "Development")

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    DATABASE_HOST = os.getenv("DATABASE_HOST")
    DATABASE_PORT = os.getenv("DATABASE_PORT")
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    DATABASE_USER = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

# Single shared settings object
settings = Settings()