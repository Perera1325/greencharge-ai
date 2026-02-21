import jwt
import datetime

private_key = open("ballerina-orchestrator/orchestrator/certs/private.key").read()

payload = {
    "iss": "greencharge",
    "aud": "ev-clients",
    "sub": "vinod",
    "role": "admin",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
}

token = jwt.encode(payload, private_key, algorithm="RS256")

print(token)