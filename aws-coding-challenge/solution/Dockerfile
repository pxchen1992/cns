# Use the official Python image as base
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY aws-coding-challenge/solution/current_time.py ./

# Install Flask
RUN pip install flask

# Expose port 80
EXPOSE 80

# Command to run the Flask application
CMD ["python", "current_time.py"]
