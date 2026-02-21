from flask import Flask, jsonify
import random

app = Flask(__name__)

ev_state = {
    "vehicle_id": "EV-101",
    "battery_level": 35,
    "location": "Colombo",
    "range_km": 120
}

@app.route("/ev/status")
def status():
    ev_state["battery_level"] = random.randint(20, 80)
    return jsonify(ev_state)

if __name__ == "__main__":
    app.run(port=5001, debug=True)