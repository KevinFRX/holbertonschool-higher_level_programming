#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the body size
curl -s "$1" | wc -c
