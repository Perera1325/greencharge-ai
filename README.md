GreenCharge AI

A Secure Distributed EV Charging Optimization System Built with Ballerina and Docker



Overview



GreenCharge AI is a distributed microservices architecture that simulates intelligent electric vehicle charging optimization. The system integrates vehicle telemetry, charging station data, and an AI-based optimization engine through a secure Ballerina orchestration layer.



The orchestrator service is protected using JWT-based authentication and coordinates all internal services securely inside a Docker network.



Architecture



The system consists of four services:



EV Simulator

Simulates vehicle battery level, consumption rate, and location.



Station Simulator

Provides station data including carbon intensity, queue length, price per kWh, and grid supply.



AI Optimization Engine

Calculates optimal charging recommendation using cost, charging time, carbon emission, and queue metrics.



Ballerina Orchestrator

Acts as a secure API gateway.

Validates JWT tokens.

Coordinates service calls.

Aggregates results and returns optimized recommendation.



Technology Stack



Ballerina 2201

Docker \& Docker Compose

Python (Flask microservices)

JWT with RS256 (public/private key validation)



Security Layer



The orchestrator endpoint requires a valid RS256 signed JWT token.



Token validation includes:

Issuer verification

Audience validation

Signature verification using RSA public key



Only authenticated clients can access:



GET /orchestrator/recommend



This demonstrates how Ballerina can function as a lightweight secure API gateway in distributed systems.



Why Ballerina



Ballerina is particularly suited for this architecture because:



Native HTTP client/server support

Built-in JWT and OAuth2 capabilities

Network-first design

Strong typing for JSON contracts

Seamless microservice orchestration



In this project, Ballerina functions as:



Service orchestrator

API gateway

Security enforcement layer



System Flow



Client → JWT Authentication → Ballerina Orchestrator → EV Service → Station Service → AI Engine → Aggregated Response



How to Run



docker compose build

docker compose up



Generate token:



python generate\_token.py



Call API:



curl -H "Authorization: Bearer YOUR\_TOKEN" http://localhost:8080/orchestrator/recommend



Project Objective



This project explores how distributed EV charging systems can be optimized using secure orchestration and intelligent decision-making while maintaining API-level security and service isolation.



