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
    """
    Central application settings.
    """

    # Application information
    APP_NAME = os.getenv("APP_NAME", "Production GitOps API")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "Development")

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # Database (used later)
    DATABASE_URL = os.getenv("DATABASE_URL")


# Single shared settings object
settings = Settings()