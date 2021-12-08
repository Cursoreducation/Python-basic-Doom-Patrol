class Person:
    __slots__ = ('name', 'age', 'sex')


adam = Person()

adam.name = 'Adam'
adam.age = 29
adam.sex = 'Male'

print(adam.name)
print(adam.age)
print(adam.sex)
