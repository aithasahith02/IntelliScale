FROM python:3.10-slim

WORKDIR /app

COPY controller.py ./

RUN pip install requests

CMD ["python", "controller.py"]


