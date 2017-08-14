#!/usr/bin/python
"""
    @author: MinhHT3
    @brief: Generator
"""

def count_down(x):
    i = 5
    while i > 0:
        yield i
        i -= 1
for i in count_down(5):
    print(i)

# infinite sevens
# def infinite_sevens():
#     while True:
#         yield 7
# for i in infinite_sevens():
#     print(i)

def numbers(x):
    for i in range(x):
        if i % 3 == 0:
            yield i
print(list(numbers(10)))

