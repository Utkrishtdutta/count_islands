# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements file if you have any dependencies
# COPY requirements.txt ./

# Install the dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Specify the default command to run the script
ENTRYPOINT ["python", "./scripts/main.py"]
CMD ["input.txt"]  
