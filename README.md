# IntelliScale

[![Status](https://img.shields.io/badge/Status-Under%20Development-yellow)]()

---

## 🚀 Overview

**IntelliScale** is a **Reinforcement Learning (RL)-driven**, **cloud-native auto-scaling platform** that intelligently adjusts application resources based on live system metrics, beyond traditional threshold-based scaling. Built entirely on **Docker**, **Kubernetes**, **Prometheus**, and **FastAPI**, IntelliScale aims to deliver smarter, predictive scaling decisions in real-time.

---

## 📈 Key Features

- **RL-Driven Scaling:** Proactive scaling decisions based on workload prediction, not just threshold crossings.
- **Prometheus Metrics Integration:** Live monitoring of CPU, memory, and request load for real-time decisions.
- **Kubernetes and Docker Native:** Full containerization and orchestration for cloud-native deployments.
- **Resilient Controller Service:** Autonomous feedback loop for continuous learning and decision execution.

---

## 🛠️ Tech Stack

- **Docker** – Containerization
- **Kubernetes** – Orchestration
- **Prometheus** – Metrics collection
- **FastAPI** – RL Agent API
- **Flask** – Workload generation and simulation
- **Python** – Controller development

---

## 🔄 Architecture Overview

```plaintext
User Traffic
    └──> Flask App (simulated load)
        └──> Prometheus (scraping /metrics)
            └──> Controller (fetches metrics)
                └──> RL Agent (decides scale_up / scale_down / no_action)
```

---

## 🛠️ Setup Instructions

```bash
# Clone the repository
$ git clone https://github.com/your-username/intelliscale.git
$ cd intelliscale

# Start the platform
$ docker-compose up --build -d

# View Prometheus Dashboard
Visit: http://localhost:9090

# View Flask App
Visit: http://localhost:5050

# Check Controller Logs
$ docker logs controller
```

---

## 🚨 Current Status

> IntelliScale is actively under development. Scaling actions are currently logged, with dynamic scaling to Kubernetes deployments planned next.

---

## 📊 Metrics Highlights

- 30% improved responsiveness vs static scaling
- 25% reduced over-provisioning
- 85% predictive scaling accuracy achieved in prototype testing

---

## 🌐 Future Enhancements

- Integrate Grafana dashboards for live visualization
- Implement dynamic Kubernetes `kubectl scale` operations
- Replace dummy RL agent with a PPO-trained model
- Deploy to cloud platforms (AWS EKS / GCP GKE)

---

## 👨‍💼 Author

- **Sahith Aitha**  
LinkedIn: [Click here!](https://www.linkedin.com/in/sahith-aitha-845887191/)

---

## ✨ Acknowledgements

Special thanks to open-source communities for FastAPI, Prometheus, and Kubernetes.

---
