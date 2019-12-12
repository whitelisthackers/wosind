#!/bin/bash

DOMAIN=$1
IPADDR=$2

rm -f tmp/erg_dom.txt
rm -f tmp/erg_ip.txt
rm -f tmp/cleared_erg.txt

whois $DOMAIN > tmp/erg_dom.txt
whois $IPADDR > tmp/erg_ip.txt
