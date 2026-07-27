"""
API Routes

This file contains all public API endpoints.

Keeping routes in a separate file makes the project
cleaner and easier to maintain as it grows.
"""

from fastapi import APIRouter
from app.config.settings import settings

# Create a router object
router = APIRouter()


@router.get("/")
def read_root():
    """
    Root endpoint.

    Used to verify that the API is running.
    Returns the current deployment environment.
    """

    return {
        "status": "Success",
        "message": "Welcome to the Production GitOps Pipeline API!",
        "environment": settings.ENVIRONMENT
    }


@router.get("/health")
def health_check():
    """
    Health endpoint.

    Docker and Kubernetes use this endpoint
    to verify that the application is healthy.
    """

    return {
        "status": "healthy",
        "version": "v2.0",
        "message": "Live GitOps Deployment Success!"
    }


@router.get("/api/v1/data")
def get_data():
    """
    Sample API endpoint.

    Later this data will come from PostgreSQL.
    """

    return {
        "data": [
            {
                "id": 1,
                "item": "DevOps Core Principles"
            },
            {
                "id": 2,
                "item": "GitOps Automation with ArgoCD"
            },
            {
                "id": 3,
                "item": "Infrastructure as Code"
            }
        ]
    }