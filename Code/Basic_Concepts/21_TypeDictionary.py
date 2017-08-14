#!/usr/bin/python
"""
    @author: MinhHT3
    @brief: Type Dictionary
"""

## Dictionaries : {}
#
dict_ages = {"Minh": 25, "Hoang": 24, "Huyen": 28, "Dung": 30}
print(dict_ages["Minh"])
print(dict_ages["Hoang"])
print(dict_ages["Huyen"])
print(dict_ages["Dung"])

dict_emplty = {}
print(dict_emplty)

dict_primary = {
    "red" : [255, 0, 0],
    "green" : [0, 255, 0],
    'blue' : [0, 0, 255],
}

print(dict_primary["red"])
print(dict_primary["green"])
print(dict_primary["blue"])
# print(dict_primary["yellow"]) ; KeyError

# Dictionary functions
#
dict_squares = {1: 1, 2: 4, 3: "error", 4: 16,}
dict_squares[8] = 64
dict_squares[3] = 9
print(dict_squares)

# in, not in
dict_nums = {
    1: "one",
    2: "two",
    3: "three",
}

print(1 in dict_nums)
print("three" in dict_nums)
print(4 not in dict_nums)

# method get
dict_pairs = {
    1: "apple",
    "orange": [2, 3, 4],
    True: False,
    None: "True",
}

print(dict_pairs.get("orange"))
print(dict_pairs.get(7))
print(dict_pairs.get(123, "not in dictionary"))
