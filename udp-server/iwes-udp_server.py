import socket
from psycopg2 import connect  # published under GNU Lesser General Public License
import pandas
import atexit

# init postgres stuff
table_name = "NMEA"
connected = False

while not connected:
    try:
        conn = connect(
            dbname="iwes_challenge",
            user="iwes",
            host="iwes-postgres",
            port="5432",
            password="iwes"
        )
        cursor = conn.cursor()
        print('connection established', conn.status)
        connected = True
    except:
        continue


cursor.execute(f"CREATE TABLE IF NOT EXISTS NMEA (id SERIAL PRIMARY KEY, a TEXT, b TEXT, timestamp TEXT, status1 TEXT, d TEXT, heading TEXT, status2 TEXT, roll TEXT, status3 TEXT, pitch TEXT, status4 TEXT, HeaveRaw TEXT, status5 TEXT, HeaveLever TEXT, SurgeLever TEXT, SwayLever TEXT, HeaveSpeed TEXT, SurgeSpeed TEXT, SwaySpeed TEXT, HeadingROT TEXT, Checksum TEXT);")
print('NMEA table created')
# get column names
data_frame = pandas.read_sql_query('SELECT * FROM {} LIMIT 0'.format(table_name), conn)
table_columns = list(pandas.DataFrame.head(data_frame))

# pop sequential primary key id since it is automatically filled
table_columns.pop(0)


# define on quit behavior
def on_exit():
    # commit db changes
    conn.commit()

    # get latest table content
    cursor.execute(f'SELECT * FROM {table_name}')

    # print table
    print(table_columns)
    for i, record in enumerate(cursor):
        print('\n', record)

    # close the cursor
    cursor.close()

    # close the connection
    conn.close()


atexit.register(on_exit)

# init UDP Server
localIP = "iwes-udp_server"
localPort = 20001
bufferSize = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, localPort))
print('socket bound')

timer = 0

while timer < 10:
    print('listening')
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0].decode("utf-8")

    address = bytesAddressPair[1]

    message = '(\'' + message.replace(',','\',\'').replace('*', '\',\'*') + '\')'
    print('received:', message)

    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    try:
        cursor.execute(f"INSERT INTO {table_name}({','.join(table_columns)}) VALUES {message};")
        print('message was written to the db successfully')
    except:
        print('An exception occurred - maybe the sentence was to short. Try again.')

    timer += 1
