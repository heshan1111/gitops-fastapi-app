"""
Application Entry Point
"""

import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.config.database import engine
from app.config.settings import settings
from app.config.logger import logger
from app.routes.api import router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Real-world DevOps journey backend setup",
)


@app.on_event("startup")
def startup_event():

    for attempt in range(10):
        try:
            with engine.connect() as connection:
                connection.execute(text("SELECT 1"))

            logger.info("Connected to PostgreSQL successfully.")
            return

        except Exception as e:
            logger.warning(
                f"Waiting for PostgreSQL... ({attempt + 1}/10)"
            )
            logger.warning(str(e))
            time.sleep(3)

    raise RuntimeError("Could not connect to PostgreSQL")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

logger.info(
    f"{settings.APP_NAME} started successfully in {settings.ENVIRONMENT} environment."
)