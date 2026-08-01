from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.auth.jwt import (
    create_access_token,
    create_refresh_token,
    verify_refresh_token,
)
from app.auth.password import verify_password
from app.repositories import user_repository
from app.schemas.user import Token, UserLogin


def login(
    db: Session,
    user: UserLogin,
) -> Token:
    """
    Authenticate a user and return a JWT token.
    """

    db_user = user_repository.get_by_email(
        db,
        user.email,
    )

    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    if not verify_password(
        user.password,
        db_user.password,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        {
            "sub": db_user.email,
            "role": db_user.role,
        }
    )

    refresh_token = create_refresh_token(
        {
            "sub": db_user.email,
        }
    )

    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer",
)


def refresh_access_token(
    db: Session,
    refresh_token: str,
) -> Token:
    """
    Verify refresh token and generate a new access token.
    """

    payload = verify_refresh_token(refresh_token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )

    email = payload.get("sub")

    if email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )

    db_user = user_repository.get_by_email(
        db,
        email,
    )

    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    new_access_token = create_access_token(
        {
            "sub": db_user.email,
            "role": db_user.role,
        }
    )

    return Token(
        access_token=new_access_token,
        refresh_token=refresh_token,
        token_type="bearer",
    )