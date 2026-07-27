"""
Application Settings

This file stores all application configuration.

Instead of calling os.getenv() everywhere,
we keep all settings in one place.
"""

import os


class Settings:
    # Current application environment
    ENVIRONMENT = os.getenv("ENVIRONMENT", "Local")

    # API information
    APP_NAME = "Production GitOps API"
    VERSION = "1.0.0"


# Create a single settings object
settings = Settings()