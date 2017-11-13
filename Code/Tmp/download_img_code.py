#!/usr/bin/python
#
"""
    @author: MinhHT3
    @date: 2017-10-19
    @brief : download image
"""
from urllib.request import urlopen
import re
import os

if __name__=="__main__":
    url_list = set()

    f = urlopen("http://10.218.141.79:5000").read()
    pattern = r'href="(http://10.*)" target.* alt="(.*)"'
    match = re.findall(pattern, f.decode())
    if match:
        for item in match:
            url_list.add(item)

    # create a new folder
    path = "image"
    if not os.path.isdir(path):
        os.makedirs(path)

    # Download the file from 'url' and save it locally under 'file_name'
    for item in url_list:
        try:
            print("--------------------------------")
            print(">> " + item[1])

            f_out = open(path + "/" + item[1], 'wb')
            f_out.write(urlopen(re.sub(' ', '%20', item[0])).read())
            f_out.close()

        except:
            print("\n----- Error! -----")
    print("\nFinished!")
