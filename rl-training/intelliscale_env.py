import gymnasium as gym
from gymnasium import spaces
import numpy as np

class IntelliScaleEnv(gym.Env):
    def __init__(self):
        super(IntelliScaleEnv, self).__init__()

        self.action_space = spaces.Discrete(3)

        self.observation_space = spaces.Box(
            low=np.array([0.0, 0.0, 0.0]),
            high=np.array([100.0, 100.0, 1000.0]),
            dtype=np.float32
        )

        self.cpu = np.random.uniform(30, 50)  # Start healthy
        self.memory = np.random.uniform(30, 50)
        self.request_rate = np.random.uniform(100, 300)
        self.step_count = 0
        self.max_steps = 100  # One episode = 100 timesteps

    def reset(self, seed=None, options=None):
        self.cpu = np.random.uniform(30, 50)
        self.memory = np.random.uniform(30, 50)
        self.request_rate = np.random.uniform(100, 300)
        self.step_count = 0

        obs = np.array([self.cpu, self.memory, self.request_rate], dtype=np.float32)
        return obs, {}

    def step(self, action):
        # Simulate system dynamics
        if action == 0:  # scale_down
            self.cpu += np.random.uniform(-10, 5)
            self.memory += np.random.uniform(-5, 2)
        elif action == 2:  # scale_up
            self.cpu += np.random.uniform(-5, 10)
            self.memory += np.random.uniform(-2, 5)
        else:  # no_action
            self.cpu += np.random.uniform(-3, 3)
            self.memory += np.random.uniform(-2, 2)

        self.request_rate += np.random.uniform(-20, 20)
        self.cpu = np.clip(self.cpu, 0, 100)
        self.memory = np.clip(self.memory, 0, 100)
        self.request_rate = np.clip(self.request_rate, 0, 1000)

        self.step_count += 1

        # Reward logic
        reward = 0
        if 30 <= self.cpu <= 70:
            reward += 1  # healthy cpu
        else:
            reward -= 1  # bad cpu

        done = self.step_count >= self.max_steps
        obs = np.array([self.cpu, self.memory, self.request_rate], dtype=np.float32)

        return obs, reward, done, False, {}

    def render(self):
        print(f"CPU: {self.cpu:.2f}%, Memory: {self.memory:.2f}%, Requests/sec: {self.request_rate:.2f}")

    def close(self):
        pass

