from fastapi import FastAPI
from rl_env import DummyEnv
from prometheus_client import generate_latest
from fastapi.responses import PlainTextResponse

app = FastAPI()

env = DummyEnv()   # Instance of Dummy ENV

@app.get("/")
def root():
    return {"message": "IntelliScale RL Agent is Running!"}

# Decision API
@app.post("/decide/")
def decide(cpu: float, memory: float, request_rate: float):
    """
    Receives system metrics from the caller and returns a scaling decision.
    """
    state = [cpu, memory, request_rate]  
    action = env.decide_action(state)   
    return {"action": action}

# Metrics Endpoint for Prometheus
@app.get("/metrics")
def metrics():
    return PlainTextResponse(generate_latest())
