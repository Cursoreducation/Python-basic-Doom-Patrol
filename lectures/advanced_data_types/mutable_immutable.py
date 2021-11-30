first_var = 5
import keyword
print(keyword.kwlist)
print(keyword.iskeyword('first_var'))

b = 15
# 9789440
c = 5
b = b + c
print(id(b))
# 9789600

a = [1, 2]
print(id(a))
# 139762877595584
a[1] = 3
print(a)
print(id(a))
# 139958350593984

lst = [1, 2, 3, 'string', [1, 3], 1.2, True, {'my_value': 'value'}]
print(len(lst))
print(lst[7]['my_value'])

dct = {"Hello": "Привіт",
       "Hi": {
           "urk": "Привіт",
           "es": "Hola"
       }}
print(dct["Hi"]["es"])
lst1 = [1, 2, 4, 5, 5, 7, 7, 8, 3, 4]
st1 = set(lst1)
print(st1)
st = {1, 2, 3, 4}

# simple list of integers
lst2 = [1, 2, 3, 4]
# iterable as source
array = bytearray(lst2)
print(array)
# bytearray(b'\x01\x02\x03\x04')
print("Count of bytes:", len(array))
# Count of bytes: 4

i = 5798875656
flt = 15778.154778
cmplx = complex(2, -3)
print(cmplx)
bl = True
bl1 = False
a = None

strng = 'Srerafa 12 [fdf]'
tpl = (1, 2, 3, 3)
lst3 = [1, 2, 3]
lst3.append(4)
print(lst3)
print(tpl[1])

strg = "olalo"
print(strg)
# rng = range(1, 10)
for i in range(0, 10):
    print('Hello')

# tuple of numbers
nu = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# converting tuple to frozenset
fnum = frozenset(nu)
# frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9})
print(fnum)

x = bytes(2)
print(x)


def my_func(lst):
    lst.append(8)


my_list = [5, 6]
my_func(my_list)
print(my_list)
# [5, 6, 1]

def my_func_immutable_arg(s):
    s += "ending"
    print(s)  # prints "crazy ending"

s = "crazy "
my_func_immutable_arg(s)
print(s)  # s left unchanged, prints "crazy "

