FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies for psycopg2 and others
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source code
COPY backend/app/ /app/
# Copy the ML artifacts because model_registry expects them at ../../../ml/artifacts 
# Wait, inside the container, if the app is in /app, the relative path "../../../ml/artifacts" 
# will go to /ml/artifacts if __file__ is /app/services/model_registry.py
# __file__ = /app/services/model_registry.py
# dirname(__file__) = /app/services
# ../../../ = /
# So we should copy ml/artifacts to /ml/artifacts
COPY ml/artifacts /ml/artifacts

# Expose port
EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
