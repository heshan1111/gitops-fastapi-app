"""
API Routes

This file contains all public API endpoints.

Keeping routes in a separate file makes the project
cleaner and easier to maintain as it grows.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse,
    UserLogin,
    Token,
)
from app.services import api_service
from app.services.auth_service import login


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


@router.post(
    "/users",
    response_model=UserResponse,
    status_code=201,
)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    return api_service.create_user(db, user)


@router.post(
    "/login",
    response_model=Token,
)
def login_user(
    user: UserLogin,
    db: Session = Depends(get_db),
):
    return login(db, user)


@router.get(
    "/users",
    response_model=list[UserResponse],
)
def read_users(
    db: Session = Depends(get_db),
):
    return api_service.get_users(db)


@router.get(
    "/users/{user_id}",
    response_model=UserResponse,
)
def read_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    return api_service.get_user_by_id(db, user_id)


@router.put(
    "/users/{user_id}",
    response_model=UserResponse,
)
def update_existing_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
):
    return api_service.update_user(db, user_id, user)


@router.delete("/users/{user_id}")
def delete_existing_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    return api_service.delete_user(db, user_id)