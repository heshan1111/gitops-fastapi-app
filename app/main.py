"""
Application Entry Point

This file creates the FastAPI application,
registers middleware,
loads API routes,
and verifies the database connection at startup.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from app.config.database import Base, engine
import app.models

from app.config.settings import settings
from app.config.logger import logger
from app.config.database import engine

from app.routes.api import router

# Create FastAPI applicationggit 
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Real-world DevOps journey backend setup",
)


# Verify database connection when the application starts
@app.on_event("startup")
def startup_event():
    try:
        Base.metadata.create_all(bind=engine)

        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        logger.info("Connected to PostgreSQL successfully.")
        logger.info("Database tables created successfully.")

    except Exception as e:
        logger.error(f"Database connection failed: {e}")

# Enable Cross-Origin Resource Sharing (CORS)
app.add_middleware(
    CORSMiddleware,

    # Allow frontend applications to access the API.
    # Replace "*" with your frontend domain in production.
    allow_origins=["*"],

    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all API routes
app.include_router(router)

# Log application startup
logger.info(
    f"{settings.APP_NAME} started successfully in {settings.ENVIRONMENT} environment."
)