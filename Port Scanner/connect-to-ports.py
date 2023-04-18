"""
Check which ports are open
"""

import sys
import socket as soc
from datetime import datetime


for port in range(1, 65525):
    s = soc.soc(soc.AF_INET, soc.SOCK_STREAM)
    soc.setdefaulttimeout(1)

    # Return error
    # ERROR HERE -> result = s.connect_ex((target, port))
    # if result == 0:
    #     print("Port {} is open".format(port))

    # s.close()
