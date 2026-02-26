# Use lightweight Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (needed for many ML libs)
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first (for caching)
COPY requirements.txt .

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose Flask port
EXPOSE 3000

# Run server
CMD ["python", "main.py"]