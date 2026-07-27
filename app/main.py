"""
Application Entry Point

This file creates the FastAPI application,
registers middleware,
and loads all API routes.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.api import router

# Create FastAPI application
app = FastAPI(
    title="Production GitOps API",
    version="1.0.0",
    description="Real-world DevOps journey backend setup"
)

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