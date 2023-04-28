#!/bin/bash
#To take in the URL as an argument and displays the body of the response
curl -s --header X-HolbertonSchool-User-Id:98 "$1"
