from flask import Flask, request, jsonify

app = Flask(__name__)

BATTERY_CAPACITY_KWH = 60  # average EV battery

def calculate_energy_needed(battery_level):
    missing_percentage = 100 - battery_level
    energy_needed = (missing_percentage / 100) * BATTERY_CAPACITY_KWH
    return round(energy_needed, 2)

def estimate_charging_time(energy_needed, available_kw):
    if available_kw == 0:
        return 999
    return round(energy_needed / available_kw, 2)

def calculate_carbon_emission(energy_needed, carbon_intensity):
    # kg CO2 per kWh * energy
    return round(energy_needed * carbon_intensity, 2)

def calculate_score(station, battery):

    energy_needed = calculate_energy_needed(battery)

    charging_time = estimate_charging_time(
        energy_needed,
        station["solar_available_kw"] + station["grid_supply_kw"]
    )

    carbon_emission = calculate_carbon_emission(
        energy_needed,
        station["carbon_intensity"]
    )

    cost_factor = station["price_per_kwh"] * energy_needed
    queue_penalty = station["queue"] * 5

    score = (
        200
        - cost_factor
        - (charging_time * 10)
        - (carbon_emission * 2)
        - queue_penalty
    )

    return score, energy_needed, charging_time, carbon_emission


@app.route("/optimize", methods=["POST"])
def optimize():

    data = request.json
    battery = data["battery_level"]
    stations = data["stations"]

    best_station = None
    best_score = -999999
    detailed_results = []
    best_details = None

    for s in stations:

        score, energy_needed, charging_time, carbon_emission = calculate_score(s, battery)

        explanation = (
            f"Energy required: {energy_needed} kWh. "
            f"Estimated charging time: {charging_time} hours. "
            f"Carbon emission impact: {carbon_emission} kg CO2. "
            f"Queue length: {s['queue']}. "
            f"Price per kWh: {s['price_per_kwh']}."
        )

        result = {
            "station_id": s["station_id"],
            "score": round(score, 2),
            "energy_needed_kwh": energy_needed,
            "charging_time_hours": charging_time,
            "carbon_emission_kg": carbon_emission,
            "explanation": explanation
        }

        detailed_results.append(result)

        if score > best_score:
            best_score = score
            best_station = s
            best_details = result

    return jsonify({
        "recommended_station": best_station,
        "metrics": best_details,
        "all_station_analysis": detailed_results,
        "system_message": "Optimization completed using cost, time, carbon, and queue factors."
    })


if __name__ == "__main__":
    app.run(port=5003, debug=True)