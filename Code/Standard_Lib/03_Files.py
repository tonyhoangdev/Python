#!/usr/bin/python
#
"""
    @author: MinhHT3
    @brief : FILES
"""

import glob, os

os.chdir("/d/")

for file in glob.glob("*.py"):
    print(file)

# for root, dirs, files in os.walk("D:/"):
#     x = 0
#     for file in files:
#         if file.endswith(".pptx"):
#             x += 1

# print(x)
