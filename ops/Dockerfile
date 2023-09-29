# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /usr/src

# Copy the parent directory contents and requirements.txt into the container
COPY ops/requirements.txt requirements.txt
COPY . .


# Install the required packages
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install uvicorn

# Make port 80 available to the world outside this container
EXPOSE 80

# Define the command to run the app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]