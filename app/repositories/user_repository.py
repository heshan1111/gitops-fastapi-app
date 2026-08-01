from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

def create(
    db: Session,
    user: UserCreate,
    hashed_password: str,
) -> User:

    db_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password,
        role="user",
)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_all(db: Session) -> list[User]:
    return db.query(User).all()


def get_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()


def update(
    db: Session,
    user: User,
    updated_user: UserUpdate,
) -> User:

    user.name = updated_user.name
    user.email = updated_user.email

    db.commit()
    db.refresh(user)

    return user

def delete(db: Session, user: User) -> None:
    db.delete(user)
    db.commit()

def get_by_email(
    db: Session,
    email: str,
) -> User | None:

    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )