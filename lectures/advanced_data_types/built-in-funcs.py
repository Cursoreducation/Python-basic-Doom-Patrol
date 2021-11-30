foo = 5
print(id(foo))

our_lst = set()
print(type(our_lst))

lst = [1, 2, 3]
tpl = (1, 2, 3)
dct = {1: 'one', 2: 'two', 3: 'three'}
st = {1, 2, 3}

print(type(lst) is list)
# True
print(type(tpl) is tuple)
# True
print(type(dct) is dict)
# True
print(type(st) is set)
# True
print(type(lst) is tuple)
# False
a = 4
b = 5
prog = f'print("The sum of {a} and {b} is", (a+b))'
print(prog)
exec(prog)
# The sum of 5 and 10 is 15