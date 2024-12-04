# Use the official Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY flask_app ./flask_app

# Expose port 8080
EXPOSE 8080

# Run the Flask app
CMD ["python", "flask_app/__init__.py"]
