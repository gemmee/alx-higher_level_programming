#!/bin/bash
# A bash script that takes in a URL, sends a GET request to that URL, and displays the size(in bytes) of the body of the response.
curl -sI "$1" | grep "Content-Length:" | cut -d ' ' -f 2
