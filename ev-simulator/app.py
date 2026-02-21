from flask import Flask, jsonify
import random

app = Flask(__name__)

def generate_ev_state():

    battery = random.randint(20, 80)

    energy_consumption_rate = 0.18  # kWh per km
    range_km = int((battery / 100) * 60)

    return {
        "vehicle_id": "EV-101",
        "battery_level": battery,
        "location": "Colombo",
        "range_km": range_km,
        "consumption_kwh_per_km": energy_consumption_rate
    }

@app.route("/ev/status")
def status():
    return jsonify(generate_ev_state())

if __name__ == "__main__":
    app.run(port=5001, debug=True)