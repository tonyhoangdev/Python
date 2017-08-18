#!/usr/bin/python
#
"""
    @author: MinhHT3
    @brief : urllib
"""
from urllib.request import urlopen, Request

contents = urlopen('http://www.dr-chuck.com/page1.htm').read()
contents2 = urlopen('http://www.dr-chuck.com/page2.htm').read()

print(len(contents))
print(contents)
print(contents2)

