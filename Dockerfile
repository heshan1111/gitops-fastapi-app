# app-repo/Dockerfile

# --- Stage 1: Build & Dependency Installation ---
FROM python:3.11-slim AS builder

WORKDIR /app

# Compiler tools & dependencies install 
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Requirements file copy & packages install 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# --- Stage 2: Final Secure Production Image ---
FROM python:3.11-slim AS final

WORKDIR /app

# Copy only the python packages installed in the builder stage (reduces image size)
COPY --from=builder /usr/local /usr/local
COPY . .

# Create Environment paths 
ENV ENVIRONMENT=Production

# Security:stop runnig as root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

#  Open Runnig API server on port 8000
EXPOSE 8000

# App up command 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]