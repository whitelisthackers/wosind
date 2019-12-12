#!/usr/bin/python

from shell import shell
import sys
import socket
import warnings
warnings.filterwarnings("ignore")

erg_dom = []
clear_erg = []
erg_ip = []

def do_whois(param):

    ipaddr = socket.gethostbyname(param)
    erg = shell("./curl_call.sh %s %s %s" % (param, ipaddr))
    
    try:
        fh_dom = open("tmp/erg_dom.txt", "r")
    except:
        print "Keine Daten oder die Datei erg_dom.txt gefunden"
        sys.exit()
    clear_erg.append("\nWhois Abfrage mit dem Domainnamen")
    clear_erg.append("\n")
    for line in fh_dom:
        erg_dom.append(line)
        clear_erg.append(line)
    fh_dom.close()
       
    try:
        fh_ip = open("tmp/erg_ip.txt", "r")
    except:
        print "Keine Daten oder die Datei erg_dom.txt gefunden"
        sys.exit()
    clear_erg.append("\nWhois Abfrage mit der IP Adresse")
    clear_erg.append("\n")
    for line in fh_ip:
        if line in erg_dom:
            pass
        else:
            erg_ip.append(line)
            clear_erg.append(line)
    fh_ip.close()   

    fh_clear = open("tmp/cleared_erg.txt", "w")
    for i in clear_erg:
        print i.rstrip()
        fh_clear.write(i)