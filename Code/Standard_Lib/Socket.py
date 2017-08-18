#!/usr/bin/python
#
"""
    @author: MinhHT3
    @brief : Socket
"""

import socket

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(("www.py4inf.com", 80))

my_sock.send('GET http://www.py4inf.com/code/remeo.txt HTTP/1.0\n\n')

while True:
    data = my_sock.recv(512)
    if (len(data) < 1):
        break

    print(data)
my_sock.close()
