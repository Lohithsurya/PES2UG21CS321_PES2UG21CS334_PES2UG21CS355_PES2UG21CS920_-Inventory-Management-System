# Use an appropriate base image (e.g., Python)
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

EXPOSE 5000

# Command to run the producer script
CMD ["python", "producer.py"]



