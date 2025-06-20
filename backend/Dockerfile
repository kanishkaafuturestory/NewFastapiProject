# 1. Use an official lightweight Python image
FROM python:3.11-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy requirements and install them
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of your backend code
COPY . .

# 5. Command to run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5050"]

