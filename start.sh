#!/bin/bash

wert="y"

python wosind.py

while [ "$wert" = "y" ]

do
	read -p "Do you want to perform a testrun (y/n)? " wert
	
	if [ "$wert" = "n" ]
	then
		exit 0
	else
		python wosind.py
	fi
done
