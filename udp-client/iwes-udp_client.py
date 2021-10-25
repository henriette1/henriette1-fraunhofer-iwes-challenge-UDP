import socket
import random
from time import sleep

serverAddressPort = ("iwes-udp_server", 20001)

bufferSize = 1024

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket

while True:
    sleep(5)
    message_list = [
    '$PHOCT,01,192621.400,T,00,080.378,T,-000.106,T,-03.105,T,+00.220,T,+00.084,-00.025,+00.013,+00.235,+00.024,+00.078,-0008.03*09',
    '$PHOCT,01,192621.500,T,00,080.311,T,-000.237,T,-03.066,T,+00.239,T,+00.105,-00.021,+00.020,+00.172,+00.042,+00.073,-0061.95*0D',
    '$PHOCT,01,192621.600,T,00,080.274,T,-000.329,T,-02.938,T,+00.252,T,+00.123,-00.017,+00.027,+00.205,+00.048,+00.061,+0001.33*0C',
    '$PHOCT,01,192621.700,T,00,080.153,T,-000.438,T,-02.926,T,+00.269,T,+00.141,-00.013,+00.032,+00.128,+00.041,+00.047,-0039.36*06']

    randomMessage = message_list[int(random.uniform(0, len(message_list)))]
    print('to be sent:', randomMessage)
    bytesToSend = str.encode(randomMessage)

    try:
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        break
