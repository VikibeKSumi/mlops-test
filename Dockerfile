# 1. The Foundation: Start with a lightweight version of Linux + Python
FROM python:3.9-slim

# 2. The Workbench: Create a folder inside the container
WORKDIR /app

# 3. The Tools: Install the serving libraries
# We use the --no-cache-dir flag to keep the image small
RUN pip install --no-cache-dir fastapi uvicorn httpx

# 4. The Transfer: Copy everything from your GitHub repo into that folder
COPY . .

# 5. The Trigger: When this container starts, run this command
# Note: We run "python app.py" because your app.py now handles the server startup
CMD ["python", "app.py"]
