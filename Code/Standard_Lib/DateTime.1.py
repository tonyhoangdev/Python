#!/usr/bin/python
#
"""
    @author: MinhHT3
    @brief : Date time
"""

import os
import datetime
import time

now = datetime.datetime.now()

start = time.time()
for item in range(10000):
    print(item)
end = time.time()

print(now.strftime("%y%m%d"))
print(now.strftime("%Y-%m-%d, %H:%M:%S"))
print(now)

print(time.strftime("%d-%b-%Y %H:%M:%S  "))
print(time.strftime("%Y-%m-%d, %H:%M:%S, %z, %a %A, %b %B, %c, %I, %p  "))

print("took: {0:0.1f} seconds".format(time.clock()))
print("took: {0:0.1f} seconds".format(start))
print("took: {0:0.1f} seconds".format(end))
print("took: {0:0.1f} seconds".format(end-start))
