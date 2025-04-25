# This flask app is developed to simlulates load
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from flask import Flask

import random
import time

app = Flask(__name__)

# Regular endpoint
@app.route("/")
def index():
    time.sleep(random.uniform(0.05, 0.5)) 
    return "This is Sample Flask app by Sahith Aitha!"

# Endpoint to expose metrics to prometheus
@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

