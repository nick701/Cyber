# Trojan Malware

## What is a trojan?

A Trojan, also known as a Trojan horse or simply a "Trojan", is a type of malicious software that appears to perform a desirable function for the user prior to run or install, but instead facilitates unauthorized access to the user's computer system. Trojans can be used by attackers to gain remote access to a victim's computer, steal personal information, install additional malware or spyware, and perform other harmful actions without the user's knowledge or consent. Trojans often disguise themselves as harmless or even useful software, making them difficult to detect and remove.

## Antivirus Evasion

Trojans employ several techniques to evade detection by antivirus software, which typically analyzes viruses for code patterns and compares them to a preexisting list of signatures. Some of these techniques include encryption, compression, and the use of spaghetti code. For our purposes today, we will be dealing with a compressed malicious code.

## Contents

- cc-server.py
This is a command and control server. It opens a socket, listens for data, and writes to a file with a random name.

- malicious.py
This is the 'malicious' code. It does the following:

1. Opens a socket
2. Gets its IP through IPAPI.com
3. Uses regex to scan the file system for emails and bitcoin addresses
4. Formats the addresses using JSON & encodes it
5. Sends the data to our command and control server (cc-server)

Upon completion this file must be zipped and it’s signature saved. The tricky part of this is of course the regex which takes some creativity, but the rest can be figured out simply using documentation.

## Putting it all together

Run the command and control server followed the main file. You should see some data coming in.
