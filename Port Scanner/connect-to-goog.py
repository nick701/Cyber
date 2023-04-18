'''
Connecting to Google using a socket
'''

import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("Socket creation failed -> error %s" %(err))

# Default socket port
port = 80

try:
    host_ip =