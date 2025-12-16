# 1. The Foundation: Start with a lightweight version of Linux + Python
FROM python:3.9-slim

# 2. The Workbench: Create a folder inside the container
WORKDIR /app

# 3. The Transfer: Copy everything from your GitHub repo into that folder
COPY . .

# 4. The Trigger: When this container starts, run this command
CMD ["python", "app.py"]
