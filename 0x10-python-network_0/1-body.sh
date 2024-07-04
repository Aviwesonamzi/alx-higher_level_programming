#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of a 200 status code response
curl -s -L -o - "$1" -w "%{http_code}" | awk '/200$/{print; exit}'

