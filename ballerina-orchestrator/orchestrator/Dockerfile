FROM ballerina/ballerina:2201.13.1

WORKDIR /app

USER root

COPY . .

RUN mkdir -p /app/target
RUN chmod -R 777 /app

EXPOSE 8080

CMD ["bal", "run"]