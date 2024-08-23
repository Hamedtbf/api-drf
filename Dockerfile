# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a directory for the application
WORKDIR /app/src

# Install system dependencies required for Chrome and chromedriver
RUN apt-get update && \
    apt-get install -y wget gnupg && \
    # Add Google Chrome's official GPG key
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    # Add Google Chrome repository
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list' && \
    # Install Google Chrome and other dependencies
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    # Clean up to reduce image size
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the project files (excluding files listed in .dockerignore)
COPY . /app/

# Set permissions for chromedriver
RUN chmod +x /app/chromedriver-linux64/chromedriver

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the port for the Django app
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
