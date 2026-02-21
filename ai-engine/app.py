from flask import Flask, request, jsonify
import math

app = Flask(__name__)

def calculate_score(station, battery):

    cost_factor = station["price_per_kwh"] * 100

    queue_penalty = station["queue"] * 8

    solar_bonus = station["solar_available_kw"] * 1.5

    carbon_penalty = station["carbon_intensity"] * 50

    battery_urgency = (100 - battery) * 1.2

    score = (
        solar_bonus
        + battery_urgency
        - cost_factor
        - queue_penalty
        - carbon_penalty
    )

    return score


@app.route("/optimize", methods=["POST"])
def optimize():

    data = request.json
    battery = data["battery_level"]
    stations = data["stations"]

    best_station = None
    best_score = -999999

    station_scores = []

    for s in stations:
        score = calculate_score(s, battery)
        station_scores.append({
            "station_id": s["station_id"],
            "score": score
        })

        if score > best_score:
            best_score = score
            best_station = s

    return jsonify({
        "recommended_station": best_station,
        "score": best_score,
        "all_scores": station_scores
    })


if __name__ == "__main__":
    app.run(port=5003, debug=True)