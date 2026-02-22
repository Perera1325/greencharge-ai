import ballerina/http;

service /optimize on new http:Listener(8080) {

    resource function post optimize(http:Request req) returns http:Response|error {

        json payload = check req.getJsonPayload();

        http:Response response = new;

        response.statusCode = 200;
        response.setJsonPayload({
            message: "Optimization successful",
            received: payload
        });

        return response;
    }
}