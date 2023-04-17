import socket
import base64
import random
from string import ascii_lowercase

# TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# listen on localhost port 1337
s.bind(("127.0.0.1", 1337))

# queue up to 5 requests
s.listen(5)

print("Listening on port 1337...")

while True:
    # establish connection
    clientsocket, client_ip = s.accept()
    print("[+] received a connection from -> {}".format(client_ip))

    # get encoded data
    encoded_data = clientsocket.recv(4096)
    clientsocket.close()

    # open a file with a random name and insert the decoded data into it
    random_fd = open("".join(random.coices(ascii_lowercase), k=10), "w")
    random_fd.write(base64.b64decode(encoded_data).decode("UTF-8"))
    random_fd.close()
