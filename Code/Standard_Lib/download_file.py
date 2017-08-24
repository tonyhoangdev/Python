#!/usr/bin/python
#
"""
    @author: MinhHT3
    @brief : download file
"""
from urllib.request import urlopen, Request, urlretrieve
import urllib.request
import sys

def download_file(url, file_name='', view_percent=False):
    if view_percent:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        url_req = urlopen(req)
        is_file_type = 'application' in url_req.info()["Content-Type"]
        if is_file_type:
            file_size = url_req.info()["Content-Length"]
        else:
            file_size = '(Undefined)'
        print("Size: {0} Bytes".format(file_size))
        file_name = url.split('/')[-1]
        f_out = open(file_name, 'wb')
        file_size_dl = 0        
        block_sz = 8192

        pre_percent = 0
        percent = 0
        while True:
            buffer = url_req.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f_out.write(buffer)

            if not is_file_type:
                file_size = file_size_dl

            percent = int(file_size_dl * 100 / int(file_size))
            if pre_percent != percent:
                if percent % 5 == 0:
                    sys.stdout.write("%s%%" % percent)
                    sys.stdout.flush()
                else:
                    sys.stdout.write('.')
                    sys.stdout.flush()
                pre_percent = percent

        f_out.close()
    else:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urlopen(req).read()

        if file_name == '':
            file_name = url.split('/')[-1]

        with open(file_name, 'wb') as f_out:
                f_out.write(resp)

if __name__=="__main__":    
    url_list = set()
    url_list.add("https://www.py4e.com/lectures3/Pythonlearn-01-Intro.pptx");
    url_list.add("https://www.py4e.com/lectures3/Pythonlearn-02-Expressions.pptx");
    url_list.add("https://www.py4e.com/lectures3/Pythonlearn-03-Conditional.pptx");
    url_list.add("https://www.py4e.com/lectures3/Pythonlearn-04-Functions.pptx");
    url_list.add("https://www.py4e.com/lectures3/Pythonlearn-05-Iterations.pptx");
    url_list.add("https://www.py4e.com/lectures3/Pythonlearn-06-Strings.pptx");
    url_list.add("https://www.py4e.com/lectures3/Pythonlearn-07-Files.pptx");
    url_list.add("https://www.py4e.com/lectures3/Pythonlearn-08-Lists.pptx");
    url_list.add("https://www.py4e.com/lectures3/Pythonlearn-09-Dictionaries.pptx");
    url_list.add("https://www.py4e.com/lectures3/Pythonlearn-10-Tuples.pptx");
    url_list.add("https://www.py4e.com/lectures3/Pythonlearn-11-Regex.pptx");
    url_list.add("https://www.py4e.com/lectures3/Pythonlearn-11-Regex-Handout.txt");                    
    url_list.add("https://www.py4e.com/lectures3/Pythonlearn-12-HTTP.pptx");
    url_list.add("https://www.py4e.com/lectures3/Pythonlearn-13-WebServices.pptx");
    url_list.add("https://www.py4e.com/lectures3/Pythonlearn-14-Objects.pptx");
    url_list.add("https://www.py4e.com/lectures3/Pythonlearn-15-Databases.pptx");
    url_list.add("https://www.py4e.com/lectures3/Pythonlearn-15-Database-Handout.txt");
    url_list.add("https://www.py4e.com/lectures3/Pythonlearn-16-Data-Viz.pptx");

    # Download the file from 'url' and save it locally under 'file_name'
    for item in url_list:  
        try:         
            print("--------------------------------")
            print("Downloading... " + item)
            download_file(item, item.split('/')[-1], True)
            print("\nFinished!")
        except:
            print("\n----- Error! -----")
