# Q.3 Write a program to automate Sending HTTP Request to web server.

import requests

def send_http_request(url):
    response = requests.get(url)
    return response.status_code, response.text

# Example usage
url = "http://example.com"
status_code, content = send_http_request(url)
print(f"Status Code: {status_code}")
print("Content:", content)
