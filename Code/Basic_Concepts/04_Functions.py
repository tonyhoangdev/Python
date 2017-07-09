#!/usr/bin/python
"""
    @author: MinhHT3
    @brief: Functions
"""

# filename=input("Enter a filename: ")
filename="file_name.txt"

with open(filename) as f:
    text=f.read()

print(text)

def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

print("Number of 'r' in file: {0} times.".format(count_char(text, "r")))
print("Number of all in file: {0} times.".format(len(text)))

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))
