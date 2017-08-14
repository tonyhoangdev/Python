#!/usr/bin/python
"""
    @author: MinhHT3
    @brief: Type List
"""

## Lists : []
#
list_a = ["Hello", "World", "!" ]
print(list_a[0])
print(list_a[1])
print(list_a[2])

list_emplty = []
print(list_emplty)

list_number = 3
list_things = ["string", 0, [1, 2, list_number], 4.56]
print(list_things[1])
print(list_things[2])
print(list_things[2][2])

## List Operations
#
# reassigned
#
list_nums = [7, 7, 7, 7, 7, 7, 8]
list_nums[2] = 5;
print(list_nums)

list_nums[3] = list_nums[2]
print(list_nums[3])

# add and multiple
print(list_nums + [3, 4, 6])
print(list_nums * 3)

# to check if an item is in/not in a list, using "in" operator
list_words = ["spam", "egg", "spam", "sausage"]
print("spam" in list_words)
print("egg" in list_words)
print("tomato" in list_words)

print("sausage" not in list_words)
print("hotdog" not in list_words)

## List function
#
list_function_nums = [1, 2, 3, 3]
# append
list_function_nums.append(5)
print(list_function_nums)
# len
print(len(list_function_nums))
# insert
list_index = 1
list_function_nums.insert(list_index, "21")
print(list_function_nums)
# index
list_letters = ['x', 'i', 'n', ' ', 'c', 'h', 'a', 'o', ' ', 'c', 'a', 'c', ' ', 'b', 'a', 'n']
print(list_letters.index('a'))
print(list_letters.index('n'))
# min, max, count, remove, reverse
print(min(list_letters))
print(max(list_letters))
print(list_letters.count('a'))
print(list_letters.count('n'))
list_letters.remove('a')
print(list_letters)
list_letters.reverse();
print(list_letters)
