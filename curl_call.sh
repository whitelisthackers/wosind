#!/bin/bash

if [ $# -eq 1 ]
then
	rm -f tmp/*.*
	url=$1
	curl -s -A 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36' -H 'Content-Type: html' -X GET "$url" > tmp/erg.html
else
	DOMAIN=$1
	IPADDR=$2

	rm -f tmp/*.*

	whois $DOMAIN > tmp/erg_dom.txt
	whois $IPADDR > tmp/erg_ip.txt
fi