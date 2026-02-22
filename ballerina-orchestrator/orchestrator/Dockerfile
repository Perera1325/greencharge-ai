FROM ballerina/ballerina:2201.13.1

WORKDIR /app

# Copy only dependency files first (better caching)
COPY Ballerina.toml .
COPY Dependencies.toml .

# Pull dependencies from central
RUN bal pull ballerina/http

# Now copy full source
COPY . .

# Build normally (NO offline)
RUN bal build

EXPOSE 8080

CMD ["bal", "run"]