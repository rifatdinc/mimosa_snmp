#!/bin/bash
args=("$@")

sudo nmap -p 161 ${args[0]} -sU | awk '{print $2}' | grep open
