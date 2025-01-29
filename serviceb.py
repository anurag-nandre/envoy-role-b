import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

SERVICE_C_URL = "http://localhost:10000"  # Envoy proxy for Service C

@app.route('/')
def home():
    return "Hello from Service B!"

@app.route('/serviceB', methods=['GET'])
def call_serviceC():
    try:
        # Forward the request to Service C
        response = requests.get(f"{SERVICE_C_URL}/healthcheck", timeout=5)
        return jsonify(message="Request to Service C succeeded", serviceC_response=response.text), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify(message="Request to Service C failed", error=str(e)), 500

@app.route('/healthcheck', methods=['GET'])
def call_service_healthcheck():
    try:
        response = requests.get(f"{SERVICE_C_URL}/healthcheck", timeout=5)
        return jsonify(message="Request to healthcheck succeeded", serviceB_response=response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify(message="Request to healthcheck failed", error=str(e)), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8081))
    app.run(host='0.0.0.0', port=port)  # Service B listens on the specified port
