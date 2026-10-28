FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Intentionally runs as root for container-security scanner testing.
EXPOSE 5000
CMD ["python", "app.py"]
