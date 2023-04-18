# Port Scanner

## What is enumeration?

Enumeration refers to the process of gathering information about a target system or network in order to identify vulnerabilities and potential attack vectors. This can involve various methods such as examining network traffic, querying network services, and analyzing system logs.

The information gathered during enumeration can be used to develop a comprehensive understanding of the target system, which can in turn be used to plan and execute attacks.

## What is port scanning?

Port scanning is the process of systematically scanning a target network or system to identify open ports and services.

This can be done using specialized software tools that send packets to various ports on a target system and analyze the responses received. The results of a port scan can provide valuable information about the target system, such as what services are running and what operating system is in use.

However, port scanning can also be used by attackers to identify potential attack vectors and vulnerabilities in a system.

## Socket Programing

Sockets are communication endpoints on a network that use a specific port number. They receive and process data before sending it back. A server typically waits for a client to connect to its socket, which is usually bound to port 80. The client initiates the connection, and the two-way connection is established. In this relationship, clients request data, and servers send it back. Sockets connect to a target system's IP address and require a specific port number to establish a connection.

### How can hackers use this for malicious purposes?

Hackers can use sockets to exploit vulnerabilities in network systems and gain unauthorized access to sensitive information or control of a system. By probing open ports and identifying vulnerable services, they can use various socket-based tools and techniques to launch attacks such as port scanning, denial of service, and remote code execution. Additionally, hackers can use sockets to establish backdoors or command and control channels in compromised systems, allowing them to maintain persistent access or control even after detection and remediation attempts. It is essential to have robust security measures in place to protect against these types of attacks.

## Components

- connect-to-goog.py file:
    Creating a socket:

    To create a socket in Python for connection, two parameters are required: AF_INET and SOCK_STREAM.

    AF_INET represents the ipv4 address-family, while SOCK_STREAM refers to the connection-oriented TCP protocol.

    To establish the connection, we do the following:

    1. Create a socket with the AI_INET and SOCK_STREAM arguments
    2. Get an IP address of a website that one intends to connect to
    3. Establish a connection using the .connect command
