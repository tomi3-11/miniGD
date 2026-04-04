FROM python:3.11-slim

# Preventing python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working dir
WORKDIR /app

COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y gcc libpq-dev postgresql-client redis-tools curl && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy application code
COPY . .

# Exposing application port
EXPOSE 5000

# application runs
CMD ["flask", "run"]
    
