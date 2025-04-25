# This Dockerfile is to encapsulate flask app and expose it as a service
FROM python:3.10-slim

WORKDIR /app

COPY app.py .

RUN pip install flask prometheus_client

CMD ["python", "app.py"]

