#!/bin/bash
# Sends a GET request to a URL and displays the body of the response only if the status code is 200
curl -sL -w "%{http_code}" "$1" -o response.txt | grep -q "200$" && cat response.txt
