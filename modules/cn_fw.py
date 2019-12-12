#/usr/bin/python

from shell import shell
import warnings
warnings.filterwarnings("ignore")


def do_call(param):
    
    url = "https://viewdns.info/chinesefirewall/?domain=%s" % param
    erg = shell("./curl_call.sh %s" % url)
    fh = open("tmp/erg.html", "r")
    for line in fh.readlines():
        if "the presence of GeoDNS on this domain name" in line:
            print """
            \033[0;249;0mDNS servers in China returned different IP addresses to those returned by the root servers.
            This could indicate DNS poisoning by the Great Firewall of China.
            It could also just indicate the presence of GeoDNS on this domain name.\033[0;249;0m
                """
        if "All servers were able to reach your site" in line:
            print """
            \033[0;249;0mAll servers were able to reach your site.
            This means that your site should be accessible from within mainland China.\033[0;249;0m
                """