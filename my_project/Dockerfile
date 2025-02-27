FROM python:3.12-slim-bookworm as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements/base.txt requirements/base.txt
COPY requirements/dev.txt requirements/dev.txt
RUN pip install -r requirements/dev.txt

# Copy project files
COPY . .

# Create staticfiles directory
RUN mkdir -p staticfiles

# Make entrypoint script executable
RUN chmod +x entrypoint.sh

# Set up non-root user
RUN useradd -m appuser
USER appuser

# Run entrypoint script
CMD ["./entrypoint.sh"]