FROM ballerina/ballerina:2201.13.1

WORKDIR /app

# Copy full project
COPY . .

# Give write permission to project
RUN chmod -R 777 /app

# Build project (allow dependency update)
RUN bal build

EXPOSE 8080

CMD ["bal", "run"]