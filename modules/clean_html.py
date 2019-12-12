#/usr/bin/python
# -*- coding: utf-8 -*-

def copy_clean():
    
    fh_in = open("tmp/erg.html", "r")
    fh_out = open("tmp/erg_clean.html", "w")

    for line in fh_in.readlines():
        if "&copy;" in line:
            line = line.replace("&copy;", "")
            fh_out.write(line.rstrip())
        if "&nbsp;-&nbsp;" in line:
            line = line.replace("&nbsp;-&nbsp;", "")
            fh_out.write(line.rstrip())
        if "<img height=\"20\" alt=\"ok\" src=\"/images/ok.GIF\">" in line:
            line = line.replace("<img height=\"20\" alt=\"ok\" src=\"/images/ok.GIF\">", "O.K.")
            fh_out.write(line.rstrip())
        if "<img height=\"20\" alt=\"ok\" src=\"/images/error.GIF\">" in line:
            line = line.replace("<img height=\"20\" alt=\"ok\" src=\"/images/ok.GIF\">", "NOT O.K.")
            fh_out.write(line.rstrip())
        if "</tr></tr>" in line:
            line = line.replace("</tr></tr>", "</tr>")
            fh_out.write(line.rstrip())
        else:
            fh_out.write(line.rstrip())
            
    fh_out.close()
    fh_in.close()
