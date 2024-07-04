#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response in bytes

if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

url=$1
curl -s -o /dev/null -w "%{size_download}\n" "$url"
