FROM python:3.9.7-bullseye

ADD .. /udp_server
WORKDIR /udp_server

# install psycopg2 library with PIP
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

EXPOSE 5432
CMD [ "python3", "-u", "iwes-udp_server.py"]