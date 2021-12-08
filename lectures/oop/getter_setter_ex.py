class Person:
    name = 'Adam'


adam = Person()
print(adam.name)

print(getattr(adam, 'name'))
setattr(adam, 'age', 29)
print(adam.age)
