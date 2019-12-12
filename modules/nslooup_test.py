#/usr/bin/python
# -*- coding: utf-8 -*-

from shell import shell
clear_list_mx = []
clear_list_ns = []
domain = "imbus.de"
erg = shell("nslookup -type=mx %s" % domain)
for i in erg.output():
    if "mail" in i:
        x = i.split(" ")
        clear_list_mx.append(x[4][:-1])
print clear_list_mx

erg = shell("nslookup -type=ns %s" % domain)
for i in erg.output():
    if "nameserver" in i:
        y = i.split(" = ")
        clear_list_ns.append(y[1][:-1])       
print clear_list_ns