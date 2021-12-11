# 1. Define the id of next variables:
# int_a = 55
# str_b = 'cursor'
# set_c = {1, 2, 3}
# lst_d = [1, 2, 3]
# dict_e = {'a': 1, 'b': 2, 'c': 3}

int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))

# 2. Append 4 and 5 to the lst_d and define the id one more time.

lst_d.append(4)
lst_d.append(5)

print(id(lst_d))
# 3. Define the type of each object from step 1.

print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

# 4*. Check the type of the objects by using isinstance.

print(isinstance(int_a, int))
print(isinstance(str_b, int))
print(isinstance(set_c, set))
print(isinstance(lst_d, set))
print(isinstance(dict_e, dict))

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

# 5. With .format and curly braces {}

print("Anna has {} apples and {} peaches.".format(13, 666))

# 6. By passing index numbers into the curly braces.

print("Anna has {1} apples and {0} peaches.".format(13, 666))

# 7. By using keyword arguments into the curly braces.

print("Anna has {a_num} apples and {p_num} peaches.".format(a_num = 13, p_num = 666))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)

print("Anna has {0: 5} apples and {1: 3} peaches.".format(13, 666))

# 9. With f-strings and variables

a_num = 13
p_num = 666

print(f"Anna has {a_num} apples and {p_num} peaches.")

# 10. With % operator

print("Anna has %d apples and %d peaches." % (666, 13))

# 11*. With variable substitutions by name (hint: by using dict)

dct_fruit = {'apples': 6, 'peaches': 12}
print("Anna has %(apples)d apples and %(peaches)d peaches." % dct_fruit)

#---------------------------------------COMPREHENSIONS------------------------------------------------------
# Comprehensions:
# (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)

# 12. Convert (1) to list comprehension

lst_comp1 = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst_comp1)

# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
# 13. Convert (2) to regular for with if-else

lst2 = []
for num in range(10):
    if num % 2 == 0:
        lst2.append(num // 2)
    else:
        lst2.append(num * 10)
print(lst2)

# (3)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
# #
# 14. Convert (3) to dict comprehension.

dct_comp = {num: num ** 2 for num in range(1, 11) if num % 2 == 1 }
print(dct_comp)

# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
#
# 15*. Convert (4) to dict comprehension.

dct_comp2 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range (1,11)}
print(dct_comp2)

# (5)
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
# 16. Convert (5) to regular for with if.

dct1 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dct1[x] = x ** 3
print(dct1)

# (6)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
# 17*. Convert (6) to regular for with if-else.

dct2 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dct2[x] = x ** 3
    else:
        dct2[x] = x
print(dct2)

# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
# 18. Convert (7) to lambda function

func1 = lambda x, y: x if x < y else y
print(func1(3, 2))

# (8)
# foo = lambda x, y, z: z if y < x and x > z else y
# 19*. Convert (8) to regular function

def func2(x ,y, z):
    if y < x and x > z:
        return z
    else:
        return y
print(func2(3, 2, 1))
