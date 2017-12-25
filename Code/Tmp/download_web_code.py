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
from threading import Thread

class myThread(Thread):
    def __init__(self, curr_folder, curr_url, curr_pattern_1, curr_pattern_2):
        self._curr_folder = curr_folder
        self._curr_url = curr_url
        self._curr_pattern_1 = curr_pattern_1
        self._curr_pattern_2 = curr_pattern_2
        Thread.__init__(self)

    def run(self):
        getData(self._curr_folder, self._curr_url, self._curr_pattern_1, self._curr_pattern_2)

def getData(curr_folder, curr_url, curr_pattern_1, curr_pattern_2):
    url_list = set()

    f = urlopen(curr_url).read()
    print(f.decode())
    match = re.findall(curr_pattern_1, f.decode())
    if match:
        for item in match:
            url_list.add(item)
        # print(url_list)

    # Download the file from 'url' and save it locally under 'file_name'
    for item in url_list:
        if (re.findall(curr_pattern_2, item[0])):
            try:
                print("--------------------------------")
                print(">> name: " + item[0])
                print(">>> save: " + curr_folder + "/" + item[0])
                print(">>> link: " + curr_url + "/" + item[0])

                f_out = open(curr_folder + "/" + item[0], 'wb')
                f_out.write(urlopen(curr_url + "/" + item[0]).read())
                f_out.close()
            except:
                print("\n----- Error! -----")

if __name__=="__main__":
    url_list_folder = []
    url_is_index = [0, 0, 0, 0, 1]
    url_folders = ["css", "js", "images", "photos", "index"]
    url_patterns_1 = [r'href="(.*)">(.*)</a>', r'href="(.*)">(.*)</a>', r'href="(.*)">(.*)</a>',  r'href="(.*)">(.*)</a>', r'href="(.*.html)" style.*>(.*)</a>']
    url_patterns_2 = [r'css|CSS', r'js|JS', r'jpg|JPG|png|PNG', r'jpg|JPG|png|PNG', r'.html']
    url_origin = "http://hoaqua.000webhostapp.com"

    url_index = url_origin + "/index.html"


    for item in url_folders:
        if (item != "index"):
            url_list_folder.append(url_origin + "/" + item)
        else:
            url_list_folder.append(url_origin)

    for item in url_list_folder:
        print("url_list_folder: " + item)

    threads = []
    for i in range(len(url_folders)):
        currID = i
        curr_folder = url_folders[currID]
        curr_url = url_list_folder[currID]
        curr_pattern_1 = url_patterns_1[currID]
        curr_pattern_2 = url_patterns_2[currID]

        # create a new folder
        if (not os.path.isdir(curr_folder)) and (curr_folder != "index"):
            os.makedirs(curr_folder)
        else:
            curr_folder = "."

        threads.append(myThread(curr_folder, curr_url, curr_pattern_1, curr_pattern_2))
        # getData(curr_folder, curr_url, curr_pattern_1, curr_pattern_2)

    for i in range(len(url_folders)):
        threads[i].start()

    for i in range(len(url_folders)):
        threads[i].join()

    print("\nFinished!")
