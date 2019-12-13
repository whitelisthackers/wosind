#/usr/bin/python
# -*- coding: utf-8 -*-

# version 2.2

# Fremd Module:
import sys
sys.path.append('modules/')
import platform

from spam_lists import SPAMHAUS_DBL
import ddumpster
from shell import shell
import urllib
from geopy.geocoders import Nominatim
from crtsh import crtshAPI
import json
import warnings
warnings.filterwarnings("ignore")

# wlh Module

import whois
import reverse_whois
import reverse_ip
import dnssec
import response_time
import cn_fw
import freemail
import ip_history
import reverse_mx_lookup
import reverse_ns_lookup
import propagation

if len(sys.argv) > 1:
    choice = sys.argv[1]
else:
    print """
    
        \033[1;37;40m-----------------------------------------------------------------------------------------------\033[0;32;40m
        \033[1;31;40m                     _           _ \033[0;32;40m
        \033[1;31;40m                    (_)         | |\033[0;32;40m
        \033[1;31;40m  __      _____  ___ _ _ __   __| |\033[0;32;40m
        \033[1;31;40m  \ \ /\ / / _ \/ __| | '_ \ / _` |\033[0;32;40m
        \033[1;31;40m   \ V  V / (_) \__ \ | | | | (_| |\033[0;32;40m
        \033[1;31;40m    \_/\_/ \___/|___/_|_| |_|\__,_|    version: 2.2\033[0;32;40m

          \033[1;37;40mwhitelishackers.com by [Tom]\033[0;32;40m
        \033[1;37;40m------------------------------------------------------------------------------------------------\033[0;32;40m
        
        \033[1;37;40m[1]\033[0;249;0m  DNSDumpster \033[0;37;40m(3)\033[0;32;40m
        \033[1;37;40m[2]\033[0;249;0m  Whois \033[0;37;40m(1)\033[0;32;40m
        \033[1;37;40m[3]\033[0;249;0m  Manufactor Network Interface (HEX format for a macaddress "00:00:00:00:00:00") \033[0;37;40m(4)\033[0;249;0m
        \033[1;37;40m[4]\033[0;249;0m  Ping (4 Ping from local maschine) \033[0;37;40m(1)\033[0;32;40m
        \033[1;37;40m[5]\033[0;249;0m  Testing certificates for webserver (crt.sh) \033[0;37;40m(5)\033[0;32;40m
        \033[1;37;40m[6]\033[0;249;0m  Reverse Whois \033[0;37;40m(2)\033[0;32;40m
        \033[1;37;40m[7]\033[0;249;0m  Reverse IP \033[0;37;40m(2)\033[0;32;40m
        \033[1;37;40m[8]\033[0;249;0m  DNSSEC Test \033[0;37;40m(2)\033[0;32;40m
        \033[1;37;40m[9]\033[0;249;0m  Response time from worldwide locates server to the target \033[0;37;40m(2)\033[0;32;40m
        \033[1;37;40m[10]\033[0;249;0m Header from a webserver \033[0;37;40m(1)\033[0;32;40m
        \033[1;37;40m[11]\033[0;249;0m Chinese firewall test \033[0;37;40m(2)\033[0;32;40m
        \033[1;37;40m[12]\033[0;249;0m Free Email Checkup \033[0;37;40m(2)\033[0;32;40m
        \033[1;37;40m[13]\033[0;249;0m IP history for a domain \033[0;37;40m(2)\033[0;32;40m
        \033[1;37;40m[14]\033[0;249;0m ASN search for a IP \033[0;37;40m(7)\033[0;32;40m
        \033[1;37;40m[15]\033[0;249;0m Reverse DNS (local host call) \033[0;37;40m(2)\033[0;32;40m
        \033[1;37;40m[16]\033[0;249;0m Spam DB lookup  \033[0;37;40m(8)\033[0;32;40m
        \033[1;37;40m[17]\033[0;249;0m NsLookUp Type=any \033[0;37;40m(1)\033[0;32;40m
        \033[1;37;40m[18]\033[0;249;0m NsLookUp Type=soa|a|cname|ptr|mx \033[0;37;40m(1)\033[0;32;40m
        \033[1;37;40m[19]\033[0;249;0m Portscan with local installed "nmap" (nmap -v -T4 <IP|Domain>) 
             \033[1;31;40m- Script must be started as SUDO -\033[0;249;0m
        \033[1;37;40m[20]\033[0;249;0m Vulnerability scan with local installed "nmap" (nmap -v --script vuln <IP|Domain>) 
             \033[1;31;40m- Script must be started as SUDO and can make a lot of noise on network -\033[0;249;0m
        \033[1;37;40m[21]\033[0;249;0m Reverse NS Lookup (Nameserver is needed) \033[0;37;40m(2)\033[0;32;40m
        \033[1;37;40m[22]\033[0;249;0m Reverse MX Lookup (Mailserver is needed) \033[0;37;40m(2)\033[0;32;40m
        \033[1;37;40m[23]\033[0;249;0m Check DNS propagation \033[0;37;40m(2)\033[0;32;40m
        \033[1;37;40m[24]\033[0;249;0m Decode URL \033[0;37;40m(2)\033[0;32;40m
        \033[1;37;40m[25]\033[0;249;0m GeoIP Country \033[0;37;40m(6)\033[0;32;40m
        \033[1;37;40m[26]\033[0;249;0m GeoIP City \033[0;37;40m(6)\033[0;249;0m
        Exit with \033[1;37;40m<ENTER>\033[0;32;40m
        
        \033[0;37;40m(1)\033[0;249;0m using local commands like ping, host, curl, nslookup, whois
        \033[0;37;40m(2)\033[0;249;0m using external service from https://viewdns.info
        \033[0;37;40m(3)\033[0;249;0m using external service from https://dnsdumpster.com
        \033[0;37;40m(4)\033[0;249;0m using external service from https://api.macvendors.com
        \033[0;37;40m(5)\033[0;249;0m using external service from https://crt.sh
        \033[0;37;40m(6)\033[0;249;0m using external service from https://geoip.maxmind.com
        \033[0;37;40m(7)\033[0;249;0m using external service from https://api.iptoasn.com
        \033[0;37;40m(8)\033[0;249;0m using external service from https://www.spamhaus.org/dbl/        
          """
    choice = raw_input("Enter the number of the check: ")

if choice == "1":
    param = raw_input("Enter a domain name: ")
    ddumpster.do_dump(param)

elif choice == "2":
    param = raw_input("Enter a domain name: ")
    whois.do_whois(param)
    
elif choice == "3":
    param = raw_input("Enter the macaddress: ")
    url = "https://api.macvendors.com/" + param
    erg = shell("curl -sK -X GET %s" % url)
    for i in erg.output():
        print "\033[0;249;0m" + i + "\033[0;249;0m"

elif choice == "4":
    param = raw_input("Enter a domain or ip: ")
    erg = shell("ping -c 4 %s" % param)
    for i in erg.output():
        print "\033[0;249;0m" + i + "\033[0;249;0m"
        
elif choice == "5":
    param = raw_input("Enter a domain name: ")
    print "\n  --  This check can last some minutes!  --  \n"
    try:
        print "\033[0;249;0m" + json.dumps(crtshAPI().search(param), indent=2) + "\033[0;249;0m"
    except:
        print " The service crt.sh is not available"
    print "Certificates download is ongoing!"
    shell("./crt.sh %s" % param)
    print "\033[0;249;0mThe certificate are stored as *.html files under output/crt!\033[0;249;0m"

elif choice == "6":
    print "\033[0;249;0mYou can enter a name (<john+doe>) or an emailaddress\033[0;249;0m"
    param = raw_input("Enter your searchparameter: ")
    reverse_whois.do_reverse_whois(param)
    
elif choice == "7":
    param = raw_input("Enter a domain or an IP: ")
    reverse_ip.do_call(param)
    
elif choice == "8":
    param = raw_input("Enter a domain name: ")
    dnssec.do_call(param)
    
elif choice == "9":
    param = raw_input("Enter a domain or an IP: ")
    response_time.do_call(param)

elif choice == "10":
    param = raw_input("Enter a domain name: ")
    erg = shell("curl -I -L http://%s" % param)
    print "\n"
    for i in erg.output():
        print "\033[0;249;0m" + i + "\033[0;249;0m"
        
elif choice == "11":
    param = raw_input("Enter a domain name: ")
    cn_fw.do_call(param)
    
elif choice == "12":
    param = raw_input("Enter a domain name: ")
    freemail.do_call(param)
    
elif choice == "13":
    param = raw_input("Enter a domain name: ")
    ip_history.do_call(param)
    
elif choice == "14":
    param = raw_input("Enter an IP address: ")
    erg = shell("curl https://api.iptoasn.com/v1/as/ip/%s" % param)
    for i in erg.output():
        for j in i[1:-1].split(","):
            print "\033[0;249;0m" + j + "\033[0;249;0m"
            
elif choice == "15":
    param = raw_input("Enter an IP address: ")
    erg = shell("host %s" % param)
    print "\n"
    for i in erg.output():
        print "\033[0;249;0m" + i + "\033[0;249;0m"
        
elif choice == "16":
    param = raw_input("Enter an IP address: ")
    var = param in SPAMHAUS_DBL
    if var == True:
        print "Your IP(%s) is on a SpamDatabase" % param
    else:
        print "\033[0;249;0mNo SpamDB entries for your IP (%s)\033[0;249;0m" % param
        
elif choice == "17":
    param = raw_input("Enter an IP address or a domain: ")
    erg = shell("nslookup -type=any %s" % param)
    print "\n"
    for i in erg.output():
        print "\033[0;249;0m" + i + "\033[0;249;0m"
        
elif choice == "18":
    param = raw_input("Enter a domain name or an IP address: ")
    typ = raw_input("Please choose typ of request (soa|a|cname|ptr|mx): ")
    erg = shell("nslookup -type=%s %s" % (typ, param))
    print "\n"
    for i in erg.output():
        print "\033[0;249;0m" + i + "\033[0;249;0m"
        
elif choice == "19":
    param = raw_input("\033[0;249;0mEnter a domain name or an IP address: \033[0;249;0m")
    try:
        print "This scan can last some minutes!"
        bs = platform.platform()

        if "Linux" in bs:
            erg = shell("/usr/bin/nmap -v -T4 %s" % param)
        elif "Darwin" in bs:
            erg = shell("/usr/local/bin/nmap -v -T4 %s" % param)

        print "\n"
        for i in erg.output():
            print "\033[0;249;0m" + i + "\033[0;249;0m"
    except:
        print "\033[0;249;0mScript mustbe started as SUDO or namp is not installed!\033[0;249;0m"
        
elif choice == "20":
    param = raw_input("\033[0;249;0mEnter a domain name or an IP address: ")
    try:
        print "\033[0;249;0mThis scan can last up to 10 minutes!\033[0;249;0m"
        bs = platform.platform()

        if "Linux" in bs:
            erg = shell("/usr/bin/nmap -v --script vuln %s" % param)
        elif "Darwin" in bs:
            erg = shell("/usr/local/bin/nmap -v --script vuln %s" % param)
        print "\n"
        for i in erg.output():
            print "\033[0;249;0m" + i + "\033[0;249;0m"
    except:
        print "\033[0;249;0mScript must be started as SUDO or namp is not installed!\033[0;249;0m"
        
elif choice == "21":
    try:
        param = raw_input("Enter the domain or IP address of a nameserver: ")
        reverse_ns_lookup.do_call(param)
    except:
        print "\033[0;249;0mThat IPaddress or domain is not a nameserver\033[0;249;0m"
        
elif choice == "22":
    try:
        param = raw_input("Enter the domain of a mailservers: ")
        reverse_mx_lookup.do_call(param)
    except:
        print "\033[0;249;0mThat IPaddress or domain is not a Mailserver\033[0;249;0m"

elif choice == "23":
    param = raw_input("Enter a domain name: ")
    propagation.do_call(param)

elif choice == "24":
    param = raw_input("Please enter a url string: ")
    print urllib.unquote_plus(param)
    
elif choice == "25":
    param = raw_input("Please enter an IP address: ")
    erg = shell("curl -u \"141447:Udkm6zdeXYgJ\" -X GET https://geoip.maxmind.com/geoip/v2.1/country/%s?pretty" % param)
    for i in erg.output():
        print "\033[0;249;0m" + i + "\033[0;249;0m"
        
elif choice == "26":
    georef = []
    param = raw_input("Please enter an IP address: ")
    erg = shell("curl -u \"141447:Udkm6zdeXYgJ\" -X GET https://geoip.maxmind.com/geoip/v2.1/city/%s?pretty" % param)
    for i in erg.output():
        print i
        if "latitude" in i:
            georef.append(i.lstrip()[12:-2])
        if "longitude" in i:
            georef.append(i.lstrip()[13:-2])
        
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.reverse(georef)
    print "\n"
    print "\033[0;249;0mLast known address to which IP address is assigned: \033[0;249;0m"
    print "\n"
    print "\033[0;249;0m" + (location.address) + "\033[0;249;0m"
