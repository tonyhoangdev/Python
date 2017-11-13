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
    url_list.add("https://qmlbook.github.io/assets/ch01-assets.tgz")
    url_list.add("https://qmlbook.github.io/assets/ch04-assets.tgz")
    url_list.add("https://qmlbook.github.io/assets/ch05-assets.tgz")
    url_list.add("https://qmlbook.github.io/assets/ch06-assets.tgz")
    url_list.add("https://qmlbook.github.io/assets/ch07-assets.tgz")
    url_list.add("https://qmlbook.github.io/assets/ch08-assets.tgz")
    url_list.add("https://qmlbook.github.io/assets/ch09-assets.tgz")
    url_list.add("https://qmlbook.github.io/assets/ch10-assets.tgz")
    url_list.add("https://qmlbook.github.io/assets/ch11-assets.tgz")
    url_list.add("https://qmlbook.github.io/assets/ch12-assets.tgz")
    url_list.add("https://qmlbook.github.io/assets/ch13-assets.tgz")
    url_list.add("https://qmlbook.github.io/assets/ch14-assets.tgz")
    url_list.add("https://qmlbook.github.io/assets/ch15-assets.tgz")
    url_list.add("https://qmlbook.github.io/assets/ch16-assets.tgz")

    # Download the file from 'url' and save it locally under 'file_name'
    for item in url_list:
        try:
            print("--------------------------------")
            print("Downloading... " + item)
            download_file(item, item.split('/')[-1], True)
            print("\nFinished!")
        except:
            print("\n----- Error! -----")
