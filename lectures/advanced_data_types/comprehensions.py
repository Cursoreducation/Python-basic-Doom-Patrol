lst = []
for num in range(10):
    lst.append(num*2)
print(lst)

lst_comp = [num*2 for num in range(10)]
print(lst_comp)

lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
print(lst)


lst_comp = [num ** 2 for num in range(10) if num % 2 == 1]
print(lst_comp)

lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)

list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)


lst = [("a", "b"), ("c", "d")]

d = {}
for tup in lst:
    d[tup[0]] = tup[1]

print(d)
# {'a': 'b', 'c': 'd'}

dict_comp = {k: v for k, v in lst}
print(dict_comp)
# {'a': 'b', 'c': 'd'}

dc_basic = {x: x**2 for x in [1, 2, 3, 6, 8, 9]}
print(dc_basic)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

dc_with_if = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(dc_with_if)
# {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

dc_with_elif = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dc_with_elif)
# {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}