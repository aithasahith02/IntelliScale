import requests
import time

PROMETHEUS_URL = "http://prometheus:9090"
RL_AGENT_URL = "http://rl-agent:8000/decide/"

def get_cpu_usage():
    query = 'avg(rate(process_cpu_seconds_total[1m])) * 100'
    response = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={'query': query}, timeout=5)
    result = response.json()

    try:
        cpu_value = float(result['data']['result'][0]['value'][1])
        return cpu_value
    except (IndexError, KeyError):
        return 0.0

def get_memory_usage():
    query = 'avg(process_resident_memory_bytes) / 1000000'
    response = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={'query': query}, timeout=5)
    result = response.json()

    try:
        memory_value = float(result['data']['result'][0]['value'][1])
        return memory_value
    except (IndexError, KeyError):
        return 0.0

def controller_loop():
    while True:
        try:
            cpu = get_cpu_usage()
            memory = get_memory_usage()
            request_rate = 100  # dummy

            print(f"Current CPU: {cpu:.2f}%, Memory: {memory:.2f} MB, Requests/sec: {request_rate}")

            rl_response = requests.post(RL_AGENT_URL, params={
                'cpu': cpu,
                'memory': memory,
                'request_rate': request_rate
            }, timeout=5)

            decision = rl_response.json().get('action', 'no_action')
            print(f"RL Agent Decision: {decision}")

        except Exception as e:
            print(f"[ERROR] Controller Loop Failed: {e}")

        time.sleep(10)

if __name__ == "__main__":
    controller_loop()

