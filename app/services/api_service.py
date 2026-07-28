"""
API Service Layer

This file contains the business logic of the application.

Routes should only receive requests and
delegate the work to this service.
"""
from app.config.settings import settings
from app.config.logger import logger
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


def get_home():
    """
    Return home page information.
    """

    # Log that the home endpoint was accessed
    logger.info("Home endpoint requested.")

    return {
        "status": "Success",
        "message": "Welcome to the Production GitOps Pipeline API!",
        "environment": settings.ENVIRONMENT,
    }

def get_health():
    """
    Return application health information.
    """

    # Log health check requests
    logger.info("Health endpoint requested.")

    return {
        "status": "healthy",
        "version": "v2.0",
        "message": "Live GitOps Deployment Success!",
    }


def get_learning_data():
    """
    Return sample DevOps learning data.
    """

    # Log data endpoint requests
    logger.info("Learning data endpoint requested.")

    return {
        "data": [
            {"id": 1, "item": "DevOps Core Principles"},
            {"id": 2, "item": "GitOps Automation with ArgoCD"},
            {"id": 3, "item": "Infrastructure as Code"},
        ]
    }

def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        email=user.email,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

    from typing import List

def get_users(db: Session) -> list[User]:
    logger.info("Fetching all users.")

    users = db.query(User).all()

    logger.info(f"Retrieved {len(users)} user(s).")

    return users