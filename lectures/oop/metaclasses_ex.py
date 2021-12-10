def test():
    """
    doing smth
    :return:
    """
    return {'test': 0, 'test_1': 1}


MyClass = type('MyClass', (object,), test())

obj = MyClass()
obj1 = MyClass()
print(id(obj))
print(id(obj1))
print(obj.test)
print(obj.test_1)

# class MyClass:
#     my_attr = 0
