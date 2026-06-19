# Production-Grade GitOps CI/CD Pipeline - Application Repository

This repository contains a secure, containerized FastAPI application integrated into a fully automated GitOps Continuous Integration (CI) workflow. The pipeline guarantees code quality and security by scanning for vulnerabilities before building and pushing minimal, production-ready images to Docker Hub.

---

## Tech Stack & Key Features

* Backend Framework: FastAPI (Python) with built-in health-check endpoints (/health).
* Containerization: Multi-stage Dockerfile optimized for minimal footprint and utilizing a non-root user for maximum production security.
* CI Automation: GitHub Actions workflows executing automatically on every git push.
* Security Scanning: Trivy Vulnerability Scanner integrated into the pipeline to intercept and audit security threats before artifact creation.
* Container Registry: Docker Hub hosting secure container builds.

---

## CI Pipeline Architecture Workflow

1. Local Development: Developer writes code and performs a git push to the main branch.
2. GitHub Repository: Triggers the native GitHub Actions runner environment.
3. Trivy Security Scan: Automatically intercepts and audits the code and base layers for flaws.
4. Docker Multi-stage Build: Compiles a lightweight, secure container artifact.
5. Push to Docker Hub: Securely delivers the finalized production build to the registry.

---

## Local Setup & Installation

### Prerequisites
* Python 3.10+
* Docker Desktop

### Running the Application Locally

1. Clone the repository:
git clone https://github.com/heshan1111/gitops-fastapi-app.git
cd gitops-fastapi-app

2. Build and run via Docker:
docker build -t fastapi-app:local .
docker run -p 8000:8000 fastapi-app:local

3. Verify the deployment in your browser: http://localhost:8000/health

---

## Continuous Integration (CI) Specifications

The GitHub Actions workflow configuration (.github/workflows/ci.yml) executes the following operations systematically:
1. Linting & Code Checkout
2. Trivy Vulnerability Check: Scans the repository and base layers for common configuration flaws.
3. Docker Login & Authentication: Secured natively using GitHub Repository Secrets (DOCKERHUB_USERNAME, DOCKERHUB_TOKEN).
4. Build & Push: Compiles the container image tagged with latest and target commits, pushing it seamlessly to Docker Hub.
