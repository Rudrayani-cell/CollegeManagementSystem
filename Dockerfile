# Use the official Python 3.10 base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy all files from local to container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port Cloud Run uses
EXPOSE 8080

# Command to run the app with gunicorn (production server)
CMD ["gunicorn", "-b", ":8080", "app:app"]
RUN pip install --no-cache-dir -r requirements.txt
