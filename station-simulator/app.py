from flask import Flask, jsonify
import random

app = Flask(__name__)

def generate_station(station_id, location):
    solar_kw = random.randint(5, 50)
    grid_kw = random.randint(10, 60)

    carbon_intensity = 0.85 if grid_kw > solar_kw else 0.2

    return {
        "station_id": station_id,
        "location": location,
        "solar_available_kw": solar_kw,
        "grid_supply_kw": grid_kw,
        "carbon_intensity": carbon_intensity,
        "price_per_kwh": round(random.uniform(0.18, 0.30), 2),
        "queue": random.randint(0, 5)
    }

@app.route("/stations")
def get_stations():
    stations = [
        generate_station("ST-01", "Colombo"),
        generate_station("ST-02", "Negombo"),
        generate_station("ST-03", "Kandy")
    ]
    return jsonify(stations)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)