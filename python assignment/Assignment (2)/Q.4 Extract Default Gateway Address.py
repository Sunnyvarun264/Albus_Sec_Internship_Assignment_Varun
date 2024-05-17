# Q.4 Write a Python script that extracts the default gateway address from the output of ifconfig or ipconfig and displays it to the user.

import os
import re

def get_default_gateway():
    if os.name == "nt":  # For Windows
        output = os.popen("ipconfig").read()
    else:  # For Unix/Linux
        output = os.popen("ifconfig").read()
    
    gateway = re.search(r"Default Gateway[.\s:]*([0-9.]+)", output)
    if gateway:
        return gateway.group(1)
    else:
        return "Default Gateway not found."

# Example usage
default_gateway = get_default_gateway()
print("Default Gateway:", default_gateway)
