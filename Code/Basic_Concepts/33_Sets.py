#!/usr/bin/python
"""
    @author: MinhHT3
    @brief: Sets
"""

## Sets : {} : set()
num_sets = {1, 2, 3, 4, 5, 2, 4, 11}
num_sets.add(-3)
num_sets.remove(2)
print(num_sets)

word_sets = list(set(["spam", "eggs", "sausage", "spam"]))
print(word_sets)

# Operation
a = {1, 2, 3, 4, 5, 6}
b = {0, 4, 5, 6, 7, 8, 9}
print(a | b)
print(a & b)
print(a - b)
print(b - a)
print(a ^ b)
