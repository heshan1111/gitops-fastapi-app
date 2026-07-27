"""
API Service Layer

This file contains the business logic of the application.

Routes should only receive requests and
delegate the work to this service.
"""

from app.config.settings import settings


def get_home():
    """
    Return home page information.
    """

    return {
        "status": "Success",
        "message": "Welcome to the Production GitOps Pipeline API!",
        "environment": settings.ENVIRONMENT,
    }


def get_health():
    """
    Return application health information.
    """

    return {
        "status": "healthy",
        "version": "v2.0",
        "message": "Live GitOps Deployment Success!",
    }


def get_learning_data():
    """
    Return sample DevOps learning data.
    """

    return {
        "data": [
            {"id": 1, "item": "DevOps Core Principles"},
            {"id": 2, "item": "GitOps Automation with ArgoCD"},
            {"id": 3, "item": "Infrastructure as Code"},
        ]
    }