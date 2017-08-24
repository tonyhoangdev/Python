#!/usr/bin/python
#
"""
    @author: MinhHT3
    @brief : Parsing csv files
"""
import csv

with open('numbers.csv') as f_in:
    with open ('numbers_new.csv', 'w') as f_out:
        r = csv.reader(f_in)
        w = csv.writer(f_out)
        for row in r:
            w.writerow(row)
