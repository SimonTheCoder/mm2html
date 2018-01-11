#!/usr/bin/env python
#coding=utf-8

__author__ = "Simon Shi"


import sys
import xml.etree.ElementTree as ET


def debug(info):
    print >>sys.stderr,info

def genHTML(elem):
    if len(elem) == 0:
        debug("Leaf found. TEXT=%s"% elem.get("TEXT"))
        return "<li>%s</li>" % elem.get("TEXT")
    
    ret_html = """<li>%s</li><ul>%s</ul>"""
    
    li_html = ""
    for e in elem:
        li_html = li_html + "" + genHTML(e)
    
    return ret_html % (elem.get("TEXT"), li_html)

def convert(filename):
    tree = ET.parse(filename)

    result =  """<html><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />""" + genHTML(tree.getroot()[0])+"</html>"
    return result

if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print >>sys.stderr,"usage:"
        print >>sys.stderr,"python mm2html.py xxxx.mm  yyyy.html"
        exit(1)
    res = convert(sys.argv[1])
    with open(sys.argv[2],"w") as out_fd:
        out_fd.write(res.encode(encoding="utf_8"))


