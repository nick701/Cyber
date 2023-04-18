import socket as soc
import sys


def find_service_name():
    protocolname = "tcp"
    for port in [80, 25]:
        print(
            "Port: %s -> service name: %s"
            % (port, soc.getservbyport(port, protocolname))
        )

    print("Port: %s -> service name: %s" % (53, soc.getservbyport(53, "udp")))


# Defining a target
if len(sys.argv) == 2:
    # Translate hostname to IPv4
    target = soc.gethostbyname(sys.argv[1])
else:
    print("Invlaid amount of argument")

ports = []

try:
    # Scanns for ports between 1 - 65,535
    for port in range(1, 65535):
        ports[port - 1] = port

    find_service_name(ports)

except KeyboardInterrupt:
    print("\n Exiting Program")
    sys.exit()

except soc.gaierror:
    print("\n Hostname could not be resolved")
    sys.exit()

except soc.error:
    print("\ Server not responding")
    sys.exit()
