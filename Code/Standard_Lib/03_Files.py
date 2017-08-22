#!/usr/bin/python
#
"""
    @author: MinhHT3
    @brief : FILES
"""
import os
import shutil

path=r"d:\04_Projects\ASDK-S32_SDK\sdk_codebase"
copy_to = r"d:\04_Projects\ASDK-S32_SDK\sdk_codebase_temp"
module_name = 'PinSettings'
new_module_name = 'Pins'
count = 0
for root, dirs, files in os.walk(path, topdown=True):
    count += 1
    # print(root)
    # print(dirs)
    # print(files)
    for name in files:
        src_file_path = os.path.join(root, name)
        dst_file_path = src_file_path.replace(path, copy_to)
        dst_file_path = dst_file_path.replace(module_name, new_module_name)       
        dst_dir_path = os.path.dirname(dst_file_path)       
        
        if module_name in src_file_path:
            if not os.path.exists(dst_dir_path):
                os.makedirs(dst_dir_path)
            shutil.copy(src_file_path, dst_file_path)

print("Number of folder:", str(count))
