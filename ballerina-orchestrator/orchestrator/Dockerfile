FROM ballerina/ballerina:2201.8.0

WORKDIR /app

COPY . .

# Pull dependencies first
RUN bal pull ballerina/http

# Then build
RUN bal build

EXPOSE 8080

CMD ["bal", "run"]