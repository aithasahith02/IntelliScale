from intelliscale_env import IntelliScaleEnv
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env

def main():
    # Environment creation
    env = IntelliScaleEnv()
    check_env(env, warn=True)
    model = PPO("MlpPolicy", env, verbose=1)
    
    # Train the model
    model.learn(total_timesteps=10000)

    # Save the trained model for the controller
    model.save("ppo_intelliscale")

    print("Training completed and model saved!")

if __name__ == "__main__":
    main()

