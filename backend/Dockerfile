FROM python:alpine

# Set working directory
WORKDIR /app/src

# Copy application code
COPY . /app

# Install dependencies for MariaDB connector (using apk)
RUN apk update && apk add --no-cache mariadb-dev build-base

# Install Python dependencies
RUN pip install -r /app/requirements.txt

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
