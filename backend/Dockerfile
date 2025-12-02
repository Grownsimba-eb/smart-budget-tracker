FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Copy dependency files first
COPY pyproject.toml poetry.lock* ./

# Tell Poetry to use Python 3.11 (now that pyproject.toml is present)
RUN poetry env use python3.11

# Install dependencies
RUN poetry install --no-root



# Copy the rest of the project
COPY . .

# Run FastAPI with Uvicorn
CMD ["poetry", "run", "uvicorn", "smart_budget_tracker_backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
