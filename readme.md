Readme for "wosind.py"

This software is licensed under GPL(GNU GPLv3).

This tool combines a lot of possibilties of OpenSource Intelligence.
The tool uses local shell commands, like ping, host ... and external resources as nmap
or external webservices.


1. System prerequisites
 
 - MacOS oder Linux (windows can be used only limited due to missing linux shell commands)
 - Python 2.7.x
 - Nmap (https://nmap.org/download)
 
 Python integrated modules:
 
 - urllib
 - sys
 - platform (OS detection for nmap scan)

 External python modules:
 
 - shell (https://pypi.org/project/shell/)
 - dnsdumpster (https://github.com/PaulSec/API-dnsdumpster.com)
 - spam-list (https://pypi.org/project/spam-lists/)
 - beautifulsoup4 (https://pypi.org/project/beautifulsoup4/)
 - geopy (https://geopy.readthedocs.io/en/latest/)
 - crtsh ()
 
 Own python modules:
 
 - asn_tool
 - clean_html
 - cn_fw
 - ddumpster
 - dnssec
 - freemail
 - ip_history
 - response_time
 - reverse_ip
 - reverse_whois
 - spam_db_lookup
 - whois
 - reverse_mx_lookup
 - reverse_ns_lookup
 
2. Installation
 
 Unpack "wosind.zip". 
 This *.zip package contains all necessary scripts and own modules.
 
3. Start the tool:
 
 Enter the following command in the shell:
 	<./start.sh>
 	
 
        -----------------------------------------------------------------------------------------------
                             _           _
                            (_)         | |
          __      _____  ___ _ _ __   __| |
          \ \ /\ / / _ \/ __| | '_ \ / _` |
           \ V  V / (_) \__ \ | | | | (_| |
            \_/\_/ \___/|___/_|_| |_|\__,_|    version: 2.2

          whitelishackers.com by [Tom]
        ------------------------------------------------------------------------------------------------

        1  - DNSDumpster (3)
        2  - Whois (1)
        3  - Manufactor Network Interface (HEX format for a macaddress "00:00:00:00:00:00") (4)
        4  - Ping (4 Ping from local maschine) (1)
        5  - Testing certificates for webserver (crt.sh) (5)
        6  - Reverse Whois (2)
        7  - Reverse IP (2)
        8  - DNSSEC Test (2)
        9  - Response time from worldwide locates server to the target (2)
        10 - Header from a webserver (1)
        11 - Chinese firewall test (2)
        12 - Free Email Checkup (2)
        13 - IP history for a domain (2)
        14 - ASN search for a IP (7)
        15 - Reverse DNS (local host call) (2)
        16 - Spam DB lookup (8)
        17 - NsLookUp Type=any (1)
        18 - NsLookUp Type=soa|a|cname|ptr|mx (1)
        19 - Portscan with local installed "nmap" (nmap -v <IP|Domain>) - Script must be started as SUDO -
        20 - Vulnerability scan with local installed "nmap" (nmap -v -A <IP|Domain>) - Script must be started as SUDO -
        21 - Reverse NS Lookup (Nameserver is needed) (2)
        22 - Reverse MX Lookup (Mailserver is needed) (2)
        23 - Check DNS propagation (2)
        24 - Decode URL (2)
        25 - GeoIP Country (6)
        26 - GeoIP City (6)
        Exit with <ENTER>

        (1) using local commands like ping, host, curl, nslookup, whois
        (2) using external service from https://viewdns.info
        (3) using external service from https://dnsdumpster.com
        (4) using external service from https://api.macvendors.com
        (5) using external service from https://crt.sh
        (6) using external service fromhttps://geoip.maxmind.com
        (7) using external service from https://api.iptoasn.com
        (8) using external service from https://www.spamhaus.org/dbl/  
        
Enter the number own the test you want perform        
        
After the end of the check you can prompt for another check or exit the program.

4. Special checks with "nmap":

  - nmap checks must be started with "SUDO"
  - the nmap checks can be used with OSX and linux. The tool performs
    an automatic OS detection
  - the vulnerability scan can run up to 10 minutes
  
