from functools import reduce

# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print (id(int_a))
print (id(str_b))
print (id(set_c))
print (id (lst_d))
print (id(dict_e))



# 2. Append 4 and 5 to the lst_d and define the id one more time.
print (id(lst_d.append(4)))
print (id(lst_d.append(5)))
# 3. Define the type of each object from step 1.
print (type(int_a))
print (type(set_c))
print (type(dict_e))
# 4*. Check the type of the objects by using isinstance.
print(isinstance  (int_a,int))
print(isinstance  (str_b,str))
print(isinstance  (set_c,set))
print(isinstance  (lst_d,list))
print(isinstance  (dict_e,dict))
# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."
#
# 5. With .format and curly braces {}
x = int(input("Ведіть кількість яблук:"))
y = int(input("Ведіть кількість персиків:"))
print("Anna has {} apples and {} peaces".format(x,y))
# 6. By passing index numbers into the curly braces.
print("Anna has {0} apples and {1} peaces".format('Five','Seven'))
# 7. By using keyword arguments into the curly braces.
print("Anna has {first} apples and {second} peaces".format(first='Two', second='Nine'))
# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {0:5} apples and {1:3} peaces".format(7,8))

# 9. With f-strings and variables
x = int(input("Ведіть кількість яблук:"))
y = int(input("Ведіть кількість персиків:"))
print(f"Anna has {x} apples and {y} peaces")
# 10. With % operator
x = int(input("Ведіть кількість яблук:"))
y = int(input("Ведіть кількість персиків:"))
print("Anna has %d apples and %d peaces" % (x,y))
# 11*. With variable substitutions by name (hint: by using dict)
#
# Comprehensions:
#(1)
# lst = []
# for num in range(10)
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)


# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]

# 12. Convert (1) to list comprehension
lst_comp=[num**2 if num % 2 ==1 else num**4for num in range(10) ]
print(lst_comp)
# 13. Convert (2) to regular for with if-else
lst = []
for num in range(10):
     if num % 2 == 0:
         lst.append(num // 2)
     else:
         lst.append(num * 10)
print(lst)
# (3)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)

# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)

# (5)
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}


# (6)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}

# 14. Convert (3) to dict comprehension.
dict_compr = {num: num**2 for num in range(1,11) if num%2 ==1}
print (dict_compr)
# 15*. Convert (4) to dict comprehension.
dict_compr = {num: num**2  if num % 2 == 1 else num // 0.5 for num in range(1, 11) }
print (dict_compr)
# 16. Convert (5) to regular for with if.
d = {}
for x in range(10):
    if x**3 % 4 == 0:
        d[x] = x ** 3
print(d)
# 17*. Convert (6) to regular for with if-else.
d = {}
for x in range(10):
    if x**3 % 4 == 0:
        d[x] = x ** 3
    else:
        d[x] = x
print(d)
# Lambda:
#
# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y

# (8)
# foo = lambda x, y, z: z if y < x and x > z else y

# 18. Convert (7) to lambda function
foo = lambda x, y: x if x < y else y
print(foo(10,15))
# 19*. Convert (8) to regular function
def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo(10, 15, 20))
# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
#
# 20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))
# 21. Sort lst_to_sort from max to min
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort,reverse=True))
# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(list((map(lambda x: x*2, lst_to_sort))))
# 23*. Raise each list number to the corresponding number on another list:
# list_A = [2, 3, 4]
# list_B = [5, 6, 7]
List_A=[2,3,4]
List_B=[5,6,7]
list_C=list(map(lambda numA,numB:numA**numB,List_A,List_B))
print(list_C)
# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.
import functools
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
resultat=lambda a,b:a+b
Suma_list=functools.reduce(resultat,lst_to_sort)
print(Suma_list)


# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.

lst_to_sort=[5, 18, 1, 24, 33, 15, 13, 55]
sorted_list = (list(filter(lambda x: x % 2 == 1, lst_to_sort)))
print(sorted_list)
# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
b=range(-10,10)
new_list=list(b)
print(new_list)
def neg(x):
    return x<0
neg_list=list(filter(neg,new_list))
print(neg_list)
# 27*. Using the filter function, find the values that are common to the two lists:
# list_1 = [1,2,3,5,7,9]
# list_2 = [2,3,5,6,7,8]
List_1 = [1,2,3,5,7,9]
List_2 = [2,3,5,6,7,8]

List_3=list(filter(lambda x:x in List_1,List_2))
print(List_3)
