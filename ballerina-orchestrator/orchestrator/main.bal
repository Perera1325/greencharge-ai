import ballerina/http;
import ballerina/jwt;
import ballerina/auth;

listener http:Listener httpListener = new(8080);

service /orchestrator on httpListener {

    resource function get recommend(@http:Header {name: "Authorization"} string authHeader)
            returns json|error {

        if !authHeader.startsWith("Bearer ") {
            return {
                error: "Missing or invalid Authorization header"
            };
        }

        string token = authHeader.substring(7);

        jwt:Validator validator = new({
            issuer: "greencharge",
            audience: ["ev-clients"],
            signatureConfig: {
                algorithm: jwt:RS256,
                certFile: "certs/public.crt"
            }
        });

        jwt:Payload|jwt:Error validation = validator.validate(token);

        if validation is jwt:Error {
            return {
                error: "Invalid token"
            };
        }

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