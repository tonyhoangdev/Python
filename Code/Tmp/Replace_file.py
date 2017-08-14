#!/usr/bin/python
#

import sys
import os
import shutil

family = sys.argv[1]
cpu = sys.argv[2]
newCpu = sys.argv[3]
dbPath = sys.argv[4]

print(family)
print(cpu)
print(newCpu)
print(dbPath)

cpuDBFolderPath = os.path.join(dbPath, family, cpu)
newCpuDBFolderPath = os.path.join(dbPath, family, newCpu)

print(cpuDBFolderPath)
print(newCpuDBFolderPath)

isAvailable = False
if os.path.exists(newCpuDBFolderPath):
    print("true")
    isAvailable = False
    shutil.rmtree(newCpuDBFolderPath)
else:
    print("false")
    isAvailable = True
    os.makedirs(newCpuDBFolderPath)

print("=================================================================")

def createTparFile(filePath, component, family, cpu):
    fin = open('TplinkTemplate.tplink', 'rt')
    fout = open(filePath, 'wt')
    i = 0
    for line in fin:
        line = line.replace('Family', family)
        line = line.replace('CPU', cpu)
        line = line.replace('Component', component)
        fout.write(line)
    fin.close()
    fout.close()

if (isAvailable):
    for root, dirs, files in os.walk(cpuDBFolderPath, topdown=True):
        print(root)
        print(dirs)
        print(files)
        for name in files:
            srcFilePath = os.path.join(root, name)
            dstFilePath = srcFilePath.replace(cpu, newCpu)
            dstDirPath = os.path.dirname(dstFilePath)
            if not os.path.exists(dstDirPath):
                os.makedirs(dstDirPath)
            if 'CPUCore' in dstFilePath:
                shutil.copy(srcFilePath, dstFilePath)
            else:
                baseName = os.path.basename(dstFilePath)
                component = os.path.splitext(baseName)[0]
                tparFilePath = dstFilePath.replace('tpar', 'tplink')
                createTparFile(tparFilePath, component, family, cpu)



