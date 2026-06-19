# app-repo/main.py
from fastapi import FastAPI
import os

app = FastAPI(
    title="Production GitOps API",
    version="1.0.0",
    description="Real-world DevOps journey backend setup"
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
        "status": "Healthy",
        "code": 200,
        "database_connection": "OK"
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