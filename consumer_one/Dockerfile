# Use an appropriate base image (e.g., Python)
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

EXPOSE 5001

# Command to run the consumer script
<<<<<<< HEAD
CMD ["python", "consumer_one.py"]

=======
CMD ["python", "healthcheck.py"]
>>>>>>> 4e1c931086771419fea6341f07ef7b792a45991c
