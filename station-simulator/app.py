from flask import Flask, jsonify
import random

app = Flask(__name__)

stations = [
    {
        "station_id": "ST-01",
        "location": "Colombo",
        "solar_available_kw": random.randint(10, 50),
        "price_per_kwh": 0.25,
        "queue": random.randint(0, 5)
    },
    {
        "station_id": "ST-02",
        "location": "Negombo",
        "solar_available_kw": random.randint(5, 40),
        "price_per_kwh": 0.20,
        "queue": random.randint(0, 3)
    }
]

@app.route("/stations")
def get_stations():
    return jsonify(stations)

if __name__ == "__main__":
    app.run(port=5002, debug=True)