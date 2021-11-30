def adding_number(a, b):
    return a ** b

print(adding_number(5, 6))

lmb = lambda a, b: a ** b
f = lambda: True
print(lmb(5, 6))

rand_list = [5, 7, 1, 3]
print(sorted(rand_list))
# [1, 3, 5, 7]

print(sorted(rand_list, reverse=True))
# [7, 5, 3, 1]

def foo(x):
    return x * 2

# Program to double each item in a list using map()
old_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2, old_list))
print(new_list)
# [2, 10, 8, 12, 16, 22, 6, 24]

import functools

numbers = [0, 1, 2, 3, 4]


def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


foo = functools.reduce(my_add, numbers)
# 0 + 1 = 1
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10

def filt(x):
    a = x % 2 == 0
    return a

# Program to filter out only the even items from a list
old_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(filt, old_list))
print(new_list)
# [4, 6, 8, 12]