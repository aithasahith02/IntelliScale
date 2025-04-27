from fastapi import FastAPI
from fastapi.responses import JSONResponse
from stable_baselines3 import PPO
import numpy as np
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Exposing to Prometheus
Instrumentator().instrument(app).expose(app)

# Loading the trained RL model
model = PPO.load("ppo_intelliscale.zip")

ACTION_MAPPING = {
        0: "scale_down",
        1: "no_action",
        2: "scale_up"
        }


# Decision based on RL-agent  API
@app.post("/decide/")
def decide(cpu: float, memory: float, request_rate: int):
    obs = np.array([cpu, memory, request_rate], dtype=np.float32)
    obs = obs.reshape(1, -1)
    action, _states = model.predict(obs, deterministic=True)
    action_str = ACTION_MAPPING.get(int(action), "no_action")

    return JSONResponse(content={"action": action_str})
