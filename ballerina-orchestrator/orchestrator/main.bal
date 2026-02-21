import ballerina/http;

service /orchestrator on new http:Listener(8080) {

    resource function get recommend() returns json|error {

        http:Client evClient = check new ("http://ev:5001");
        json evResponse = check evClient->get("/ev/status");

        http:Client stationClient = check new ("http://station:5002");
        json stationsResponse = check stationClient->get("/stations");

        http:Client aiClient = check new ("http://ai:5003");

        int batteryLevel = 0;

        if evResponse is map<json> {
            if evResponse.hasKey("battery_level") {
                json batteryJson = evResponse["battery_level"];
                if batteryJson is int {
                    batteryLevel = batteryJson;
                }
            }
        }

        json payload = {
            battery_level: batteryLevel,
            stations: stationsResponse
        };

        json result = check aiClient->post("/optimize", payload);

        return {
            vehicle: evResponse,
            decision: result
        };
    }
}