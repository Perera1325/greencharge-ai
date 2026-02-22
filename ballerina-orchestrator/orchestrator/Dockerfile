FROM ballerina/ballerina:2201.13.1

WORKDIR /app
COPY . .
RUN bal build

EXPOSE 8080
CMD ["bal", "run"]