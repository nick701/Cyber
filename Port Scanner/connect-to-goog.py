"""
Connecting to Google using a socket
"""

import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("Socket creation failed -> error %s" % (err))

# Default socket port
port = 80

try:
    host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror:
    # If could not resolve the host
    print("There was an error resolving the host")
    sys.exit()

# Connecting to server
s.connect((host_ip, port))


# Print the IP and port of connected server
print("The socket has successfully connected to {}:{}".format(host_ip, port))
print("IP: {}, Port: {}".format(s.getsockname()[0], s.getsockname()[1]))
