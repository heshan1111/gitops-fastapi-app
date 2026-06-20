# app-repo/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(
    title="Production GitOps API",
    version="1.0.0",
    description="Real-world DevOps journey backend setup"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "status": "Success",
        "message": "Welcome to the Production GitOps Pipeline API!",
        "environment": os.getenv("ENVIRONMENT", "Local")
    }

@app.get("/health")
def health_check():
    # health checking database connection (mocked for this example)
    return {
        "status": "healthy", 
        "version": "v2.0", 
        "message": "Live GitOps Deployment Success!"
    }
@app.get("/api/v1/data")
def get_data():
    return {
        "data": [
            {"id": 1, "item": "DevOps Core Principles"},
            {"id": 2, "item": "GitOps Automation with ArgoCD"},
            {"id": 3, "item": "Infrastructure as Code"}
        ]
    }