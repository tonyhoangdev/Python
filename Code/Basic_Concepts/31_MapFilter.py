#!/usr/bin/python
"""
    @author: MinhHT3
    @brief: Map and Filter
"""

def add_five(x):
    return x + 5

# map
nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

result = list(map(lambda x: x + 6, nums))
print(result)

# filter
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)
