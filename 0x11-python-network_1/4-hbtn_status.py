#!/usr/bin/python3
"""
Module 4-hbtn_status
Fetches https://alx-intranet.hbtn.io/status and displays the body
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
