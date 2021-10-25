FROM python:3.9.7-bullseye

ADD .. /udp_client
WORKDIR /udp_client

# install psycopg2 library with PIP
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

#EXPOSE 54321
CMD [ "python3", "-u", "iwes-udp_client.py"]