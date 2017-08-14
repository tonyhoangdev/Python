#!/usr/bin/python
"""
    @author: MinhHT3
    @brief: Itertools
"""
from itertools import count, accumulate, takewhile, product, permutations

# count
for i in count(5):
    print(i)
    if i >= 11:
        break

# accumulate <=> map, takewhile <=> filter, chain
nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x <= 10, nums)))

# product, permutations
letters = ("A", "B", "C")
print(list(product(letters, range(3))))
print(list(permutations(letters)))
print(len(list(product(letters, range(3)))))