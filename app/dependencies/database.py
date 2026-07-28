from sqlalchemy.orm import Session

from app.config.database import SessionLocal


def get_db():
    """
    Create a new database session for each request.
    """

    db: Session = SessionLocal()

    try:
        yield db
    finally:
        db.close()