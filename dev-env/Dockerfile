# dev-env/Dockerfile - for dev environment setup

FROM python:3.10-slim

# Install useful dev tools
RUN apt-get update && apt-get install -y \
    vim \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /workspace

# Install base Python packages (for both flask and RL)
RUN pip install flask fastapi uvicorn stable-baselines3 prometheus-api-client

CMD ["bash"]

