from functools import reduce
from operator import add

int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print("1.")
print(f'55 is {str(id(int_a))} \ncursor is {str(id(str_b))} \nset of 1 2 3 is {str(id(set_c))} \n'
      f'list 1 2 3 {str(id(lst_d))} \ndict "a" : 1 "b" : 2 "c" : 3 is {str(id(dict_e))}')

# 2
print("2.")
for i in range(4, 6):
    lst_d.append(i)
print(id(lst_d))

# 3
print("3.")
print("int_a = 55 : " + str(type(int_a)), end=", ")
print("str_b = cursor : " + str(type(str_b)))
print("set_c = {1, 2, 3} : " + str(type(set_c)), end=", ")
print("lst_d = [1, 2, 3] : " + str(type(lst_d)))
print("dict_e = {'a' : 1, 'b' : 2, 'c' : 3} : " + str(type(dict_e)))

# 4
print("4.")
print("int_a = 55 isinstance(var,int): " + str(isinstance(int_a, int)))
print("str_b = cursor isinstance(var,str): " + str(isinstance(str_b, str)))
print("set_c = {1, 2, 3} isinstance(var,set): " + str(isinstance(set_c, set)))
print("lst_d = [1, 2, 3] isinstance(var,(list,set)): " + str(isinstance(lst_d, (list, set))))
print("dict_e = {'a' : 1, 'b' : 2, 'c' : 3} isinstance(var,dict): " + str(isinstance(dict_e, dict)))

# 5 "Anna has ___ apples and ___ peaches." {}
print("5.")
print("Anna has {} apples and {} peaches.".format(1, 7))

# 6 "Anna has ___ apples and ___ peaches." {index}
print("6.")
print("Anna has {1} apples and {0} peaches.".format(7, 1))

# 7 "Anna has ___ apples and ___ peaches." {key}
print("7.")
print("Anna has {apple} apples and {peach} peaches.".format(apple=7, peach=1))

# 8 "Anna has ___ apples and ___ peaches."  With indicators of field size
#    (5 chars for the first and 3 for the second)
print("8.")
print("Anna has {apple:5d} apples and {peach:3d} peaches.".format(apple=7, peach=1))

# 9 .f formatting
print("9.")
apple = 7
peach = 1
print(f"Anna has {apple} apples and {peach} peaches.")

# 10 %
print("10.")
apple = 7
peach = 1
print("Anna has %s apples and %s peaches." % (apple, peach))

# 11 formatting with dictionary
print("11.")
fruits = {"a": 7, "p": 1}
print("Anna has {a} apples and {p} peaches.".format(**fruits))

# 12 list for -> comprehensions
print("12.")
lst = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst)

# 13 for comprehensions -> list:
#    list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print("13.")
list_comprehension = []
for num in range(10):
    if num % 2 == 0:
        list_comprehension.append(num // 2)
    else:
        list_comprehension.append(num * 10)
print(list_comprehension)

# 14 dict for -> comprehension
print("14.")
d = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(d)

# 15 dict for -> comprehension
print("15.")
d = {num: (num ** 2 if num % 2 == 1 else num // 0.5) for num in range(1, 11)}
print(d)

# 16 dict comprehension -> for
print("16.")
d = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d[x] = x ** 3
print(d)

# 17 dict comprehension -> for
print("17.")
d = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d[x] = x ** 3
    else:
        d[x] = x
print(d)

# 18. Convert reg func to lambda function
print("18.")
foo = lambda x, y: x if x < y else y
print(foo(2, 4))

# 19*. Convert (8) to regular function
print("19.")
def foo(x, y, z):
    if y < x and x > z:
        return z
    return y

print(foo(3, 6, 9))

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# 20. Sort lst_to_sort from min to max
print("20.")
lst_to_sort.sort()
print(lst_to_sort)

# 21. Sort lst_to_sort from max to min
print("21.")
lst_to_sort.sort(reverse=True)
print(lst_to_sort)

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print("22.")
lst_to_sort2 = list(map(lambda x: x * 2, lst_to_sort))
print(lst_to_sort2)

# 23*. Raise each list number to the corresponding number on another list:
print("23.")
list_a = [2, 3, 4]
list_b = [5, 6, 7]
list_c = list(map(lambda x, y: x + y, list_a, list_b))
print(list_c)

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.
print("24.")
sum_numbers = reduce(lambda x, y: x + y, lst_to_sort)
print(sum_numbers)

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print("25.")
lst_f = list(filter(lambda x: x % 2 == 1, lst_to_sort))
print(lst_f)

# 26. Considering the range of values: b = range(-10, 10),
#     use the function filter to return only negative numbers
print("26.")
lst_n = list(filter(lambda x: x < 0, range(-10, 10)))
print(lst_n)

# 27*. Using the filter function, find the values that are common to the two lists:
print("27.")
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
list_3 = list(filter(lambda x: x in list_2, list_1))
print(list_3)
