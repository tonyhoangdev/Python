#!/usr/bin/python
#
"""
    @author: MinhHT3
    @brief : Zip files
"""

import os
import zipfile

def get_file_zip(path):
    lst_file = []

    for root, dirs, files in os.walk(path):
        for file in files:
            lst_file.append(os.path.join(root, file))

    return lst_file
            
def zip_dir(files_path, ziph):
    # ziph is zipfile handle
    for file in files_path:
        ziph.write(file)

if __name__=='__main__':
    lst_file = get_file_zip('.')

    zipf = zipfile.ZipFile('Python3Ex.zip', 'w', zipfile.ZIP_DEFLATED)
    zip_dir(lst_file, zipf)
    zipf.close()
