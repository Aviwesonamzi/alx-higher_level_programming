#!/bin/bash
# Script that sends a JSON POST request to a URL passed as the first argument with a file's contents as the request body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
