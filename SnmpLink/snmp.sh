#!/bin/bash
args=("$@")

snmpwalk -v 1 -c public ${args[0]} ${args[1]} | awk '{print $4}' 

