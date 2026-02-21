from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_score(station, battery):
    cost_factor = station["price_per_kwh"] * 100
    queue_penalty = station["queue"] * 10
    solar_bonus = station["solar_available_kw"] * 2
    battery_urgency = (100 - battery) * 1.5

    score = solar_bonus + battery_urgency - cost_factor - queue_penalty
    return score

@app.route("/optimize", methods=["POST"])
def optimize():
    data = request.json

    battery = data["battery_level"]
    stations = data["stations"]

    best_station = None
    best_score = -999999

    for s in stations:
        score = calculate_score(s, battery)
        if score > best_score:
            best_score = score
            best_station = s

    return jsonify({
        "recommended_station": best_station,
        "score": best_score
    })

if __name__ == "__main__":
    app.run(port=5003, debug=True)