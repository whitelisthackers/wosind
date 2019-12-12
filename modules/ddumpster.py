#/usr/bin/python
# -*- coding: utf-8 -*-

from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI

def do_dump(domain):
    

    print('Testing... : {}'.format(domain))
    res = DNSDumpsterAPI(False).search(domain)
    print("\n---- Domain ----\n")
    print(res['domain'])
    
    print("\n---- DNS Servers ----\n")
    for entry in res['dns_records']['dns']:
        print(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
    
    print("\n---- MX Records ----\n")
    for entry in res['dns_records']['mx']:
        print(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
    
    print("\n---- Host Records (A) ----\n")
  
    for entry in res['dns_records']['host']:
        if entry['reverse_dns']:
            print(("{domain} ({reverse_dns}) ({ip}) {as} {provider} {country}".format(**entry)))
          
        else:
            print(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
               
    print("\n---- TXT Records ----\n")

    for entry in res['dns_records']['txt']:
        print(entry)

    map_out = "output/" + domain + "_dnsdump.png" 
    open(map_out,'wb').write(res['image_data'].decode('base64'))
    
    print "\nMap wurde gespeichert in: \n\n - %s" % map_out 
    print "\n"
