#!/usr/bin/python3
"""
Module 10-my_github
Takes your GitHub credentials (username and personal access token) and uses
the GitHub API to display your user id.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print("None")
