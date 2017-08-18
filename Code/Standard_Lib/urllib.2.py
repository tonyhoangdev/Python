#!/usr/bin/python
#
"""
    @author: MinhHT3
    @brief : urllib
"""
from urllib.request import urlopen
html = urlopen("https://www.google.com/")
print(html.read())

