# rl-agent/Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY main.py rl_env.py ./
COPY model/ ./model/
COPY ppo_intelliscale.zip .

RUN pip install fastapi uvicorn stable-baselines3 torch prometheus-fastapi-instrumentator

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

