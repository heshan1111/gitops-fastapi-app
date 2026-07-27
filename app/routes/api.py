"""
API Routes

This file contains all public API endpoints.

Keeping routes in a separate file makes the project
cleaner and easier to maintain as it grows.
"""

from fastapi import APIRouter
from app.config.settings import settings
from app.services import api_service

# Create a router object
router = APIRouter()


@router.get("/")
def read_root():
    """
    Home endpoint.
    """

    return api_service.get_home()

@router.get("/health")
def health_check():
    """
    Health endpoint.

    Docker and Kubernetes use this endpoint
    to verify that the application is healthy.
    """

    return api_service.get_health()


@router.get("/api/v1/data")
def get_data():
    """
    Sample API endpoint.

    Later this data will come from PostgreSQL.
    """

    return api_service.get_learning_data()