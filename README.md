# instructions

Make sure docker is installed and updated. Clone this repository and simply run `docker-compose up --build`.
A postgreSQL server and two python applications will start. A UDP client will send random NMEA sequences to UDP server, which will write them to the database continously.
