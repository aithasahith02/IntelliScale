# This flask app is developed to simlulates load
from flask import Flask
import random
import time

app = Flask(__name__)

@app.route("/")
def index():
    time.sleep(random.uniform(0.05, 0.5)) 
    return "This is Sample Flask app by Sahith Aitha!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

