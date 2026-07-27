# ==========================================================
# Stage 1 - Build Stage
# Install all required Python packages.
# ==========================================================
FROM python:3.11-slim AS builder

# Set the working directory inside the container
WORKDIR /app

# Install compiler tools required for some Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Copy dependency file first.
# This helps Docker cache dependencies for faster rebuilds.
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# ==========================================================
# Stage 2 - Production Image
# Create a small and secure production container.
# ==========================================================
FROM python:3.11-slim AS final

WORKDIR /app

# Python best practices
# Disable .pyc files and enable real-time logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Application environment
ENV ENVIRONMENT=Production

# Copy installed packages from builder stage
COPY --from=builder /usr/local /usr/local

# Copy application source code
COPY . .

# Create a non-root user for security
RUN useradd -m appuser && \
    chown -R appuser:appuser /app

USER appuser

# The API listens on port 8000
EXPOSE 8000

# Docker checks this endpoint to verify the container is healthy
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# Start the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]