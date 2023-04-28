#!/bin/bash
#Sends a POST request to the passed URL with data
curl -sX POST --data "email=test@gmail.com&subject=I will always be here for PLD" "$1"
