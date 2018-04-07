import socket
import random
import datetime

LOOP = 3

def echo_client(message, port):
    """
    sync tcp client
    Args:
        message: send string
        port: send tcp request to 127.0.0.0:port
    """
    print("Open: connection....")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect(('127.0.0.1', port)) 

    print('Send: %r' % message)
    client.send(message.encode())

    response = client.recv(3072)
    print('Received: %r' % response.decode())

    print('Close: tcp socket')
    client.close()


start = datetime.datetime.now()
# 8888, 8889, 8890に順番にtcpリクエストを送信
port = 8888
for i in range(0, LOOP):
    message = 'Hello World! {0}'.format(random.randint(0, 100)) 
    echo_client(message, port)
    port += 1
end = datetime.datetime.now()
print("Execution time: {0}".format(end - start))