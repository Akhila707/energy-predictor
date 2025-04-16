# Use official Python base image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy all files from current dir to /app
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the app
CMD ["python", "app/app.py"]
