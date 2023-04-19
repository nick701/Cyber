# Backdoor

## What is a backdoor?

A backdoor is a program that an attacker can install on a target machine, allowing him to access the system remotely and execute malicious commands. Installation of backdoors is usually done by exploiting vulnerabilities in the system's security. Once installed, the attacker can perform a range of malicious activities, including stealing sensitive data, installing additional malware or ransomware, or launching further attacks.

## What are shells?

Shells refer to command-line interfaces that allow users to interact with a computer system, execute commands, and manipulate files and directories.

Shells are a critical tool for conducting penetration tests, which are simulations of cyber attacks that are designed to identify vulnerabilities in computer systems. By using a shell, ethical hackers can simulate attacks on a target system, and identify potential vulnerabilities that could be exploited by real-world attackers. Shells can also be used to execute malicious commands on a target system, which is why they are often used by attackers who have gained unauthorized access to a system.

Shells create a server directly on the target machine that hackers can connect to.

Reverse shells have a client component and a server component. Clients run on the target machine already having the attacker's IP address.

## Contents

- back.py

    First, we create a server that will run on the attacker, as follows:
    1. Get out local IP and a specified port
    2. Bind the IP and port to create a socket
    3. Start listening
    4. Send and receive commands in an infinite loop
