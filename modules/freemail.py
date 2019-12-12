#/usr/bin/python

from shell import shell
import warnings
warnings.filterwarnings("ignore")


def do_call(param):
    
    url = "https://viewdns.info/freeemail/?domain=%s" % param
    erg = shell("./curl_call.sh %s" % url)
    fh = open("tmp/erg.html", "r")
    for line in fh.readlines():
        if "domain DOES NOT appear" in line:
            print "This domain DOES NOT appear to provide free email addresses"

        if "domain DOES appear" in line:
            print "This domain DOES appear to provide free email addresses."
