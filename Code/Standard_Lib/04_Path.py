#!/usr/bin/python
#
"""
    @author: MinhHT3
    @brief : OS PATH
"""

import os
import shutil


folderTest = "test1"
fileTest = 'test.txt'

currPath = os.getcwd()
print(currPath)

folderNameTest = os.path.join(currPath, folderTest)
print(folderNameTest)

fileNameTest = os.path.join(folderNameTest, fileTest)
print(fileNameTest)

abspath = os.path.abspath(fileNameTest)
print(abspath)

# Test directory
hasDir = os.path.exists(folderNameTest)
if (hasDir):
    print(folderTest + " is exists")
    shutil.rmtree(folderTest)
    print(folderTest + " have removed")
else:
    print(folderTest + " isn't exists")
    os.makedirs(folderTest)
    print(folderTest + " have created")

print('"' + folderNameTest + '"' + " is dir: " + str(os.path.isdir(folderNameTest)))
print('"{0}"{1}{2}'.format(fileNameTest ," is dir: ", str(os.path.isdir(fileNameTest))))

dirName = os.path.dirname(abspath)
baseName = os.path.basename(abspath)
ext = os.path.splitext(baseName)
ext0 = os.path.splitext(baseName)[0]
splitPath = os.path.split(abspath)

print(dirName)
print(hasDir)
print(baseName)
print(ext)
print(ext0)
print(splitPath)
