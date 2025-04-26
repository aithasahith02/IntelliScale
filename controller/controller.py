import requests
import time

# URLs for Prometheus and RL agent
PROMETHEUS_URL = "http://localhost:9090"
RL_AGENT_URL = "http://localhost:8000/decide/"

# Functions to send requests to prometheus for metrics
# Getting the CPU usage
def get_cpu_usage():
    query = 'avg(rate(process_cpu_seconds_total[1m])) * 100'
    response = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={'query': query})
    result = response.json()

    try:
        cpu_value = float(result['data']['result'][0]['value'][1])
        return cpu_value
    except (IndexError, KeyError):
        return 0.0

# Getting the memory  usage
def get_memory_usage():
    query = 'avg(process_resident_memory_bytes) / 1000000'  
    response = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={'query': query})
    result = response.json()

    try:
        memory_value = float(result['data']['result'][0]['value'][1])
        return memory_value
    except (IndexError, KeyError):
        return 0.0

# The main controller loop
def controller_loop():
    while True:
        cpu = get_cpu_usage()
        memory = get_memory_usage()
        request_rate = 100  # dummy for now

        print(f"Current CPU: {cpu:.2f}%, Memory: {memory:.2f} MB, Requests/sec: {request_rate}")

        try:
            rl_response = requests.post(RL_AGENT_URL, params={
                'cpu': cpu,
                'memory': memory,
                'request_rate': request_rate
            })

            decision = rl_response.json().get('action', 'no_action')
            print(f"RL Agent Decision: {decision}")

        except Exception as e:
            print(f"Error communicating with RL agent: {e}")

        time.sleep(10) # Runs for every 10 seconds

if __name__ == "__main__":
    controller_loop()

