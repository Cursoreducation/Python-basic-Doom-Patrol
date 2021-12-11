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