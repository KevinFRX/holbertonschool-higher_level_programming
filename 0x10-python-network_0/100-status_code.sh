#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of the response
curl -o /dev/null --silent --head --write-out "%{http_code}" "$1"
