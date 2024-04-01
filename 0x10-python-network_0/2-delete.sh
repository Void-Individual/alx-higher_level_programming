#!/bin/bash
# A bash script that sends a DELETE request to the URL passed
echo "$(curl -s -X DELETE "$1")"
