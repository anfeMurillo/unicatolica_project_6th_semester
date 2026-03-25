FROM python:3.12-slim

# Copy uv executable
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy pyproject.toml and uv.lock to install dependencies
COPY pyproject.toml uv.lock ./

# Install project dependencies
RUN uv sync --no-install-project --no-dev

# Copy project files
COPY . .

# Final sync to include project sources
RUN uv sync --no-dev


# Ensure virtual environment is in PATH
ENV PATH="/app/.venv/bin:$PATH"

# Expose port 8000
EXPOSE 8000

# Start FastAPI server
CMD ["uv", "run", "fastapi", "run", "main.py", "--port", "8000", "--host", "0.0.0.0"]
