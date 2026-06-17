# Start from an official Python image — slim variant means no unnecessary
# build tools included. Smaller image = faster pulls, smaller attack surface.
# Think of this like choosing a minimal AMI in AWS instead of a full Amazon Linux.
FROM python:3.11-slim

# Set the working directory inside the container.
# Every command after this runs from /app.
# Like doing cd /app on a server before running your app.
WORKDIR /app

# Copy requirements.txt BEFORE copying the rest of the code.
# Why? Docker builds in layers and caches each one.
# If only main.py changes, Docker reuses the cached pip install layer.
# This makes rebuilds much faster — pip install only reruns when
# requirements.txt actually changes.
# Same principle as caching node_modules in a CI pipeline.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the application code
COPY main.py .

# Document which port the app listens on.
# This doesn't actually open the port — it's just metadata.
# The actual port mapping happens in the Kubernetes Service (later).
EXPOSE 5000

# The command that runs when the container starts.
# uvicorn is the server, main:app means "the app object in main.py".
# --host 0.0.0.0 means accept connections from outside the container.
# Without 0.0.0.0 it only listens on localhost — unreachable from Kubernetes.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]