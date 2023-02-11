#!/bin/bash
# A script that takes in a URL, sends a GET request to the URL, and displays the body of the response.
curl -sI "$1" -X GET -D ./header -o ./output; if grep -q "200 OK" ./header; then cat ./output; fi
