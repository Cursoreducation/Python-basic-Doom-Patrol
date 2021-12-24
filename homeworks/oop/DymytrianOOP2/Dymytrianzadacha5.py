#1
class Laptop:
    def __init__(self):
        battery_1=Battery('electric battery capacity 5200')
        battery_2=Battery('electric battery capacity 4400')
        battery_3=Battery('electric battery capacity 10800')
        self.batterys=(battery_1,battery_2,battery_3)

class Battery:
    def __init__(self,capacity):
        self.capacity=capacity

laptop=Laptop()
print(laptop.batterys[1].capacity)
print(laptop.batterys[2].capacity)



#2
class Guitar:
    def __init__(self,guitarstring):
        self.guitarstring=guitarstring
    def printing (self):
        print(self.guitarstring)

class GuitarString:
    def __init__(self,note1,note2,note3,note4,note5,note6):
        self.note1=note1
        self.note2=note2
        self.note3=note3
        self.note4=note4
        self.note5=note5
        self.note6=note6
guitarstring=GuitarString('E','H','G','D','A','E')
guitar=Guitar(guitarstring)
guitar.printing()

#3
class Calc:
    @staticmethod
    def add_nums(param1, param2,param3):
        return print(param1 + param2+param3)
c1=Calc
c1.add_nums(10, 20,30)


#6
import dataclasses

@dataclasses.dataclass

class AddressBookDataClass:
    key:int
    name:str
    phone_number:str
    address:str
    email:str
    birthday:str
    age:int
phonebook=AddressBookDataClass(key=1,name='Andriy',phone_number='1234567',
                               address='Lviv, Shevchenka 10',email='abcd@gmail.com',birthday='01.01.91',age=25)
print(phonebook)


#7
from collections import namedtuple

AddressBookDataClass=namedtuple('AddressBookDataClass',['key','name','phone_number','adress','email','birthday','age'])
phonebook=AddressBookDataClass(1,'Andriy','1234567','Lviv, Shevchenka 10','abcd@gmail.com','01.01.91',25)
print(phonebook)

#8
class AddressBook:
    def __init__(self,key,name,phone_number,adress,email,birthday,age):
        self.key=key
        self.name=name
        self.phone_number=phone_number
        self.adress=adress
        self.email=email
        self.birthday=birthday
        self.age=age

    def __str__(self):
        return f'AdressBook {self.key}, {self.name}, {self.phone_number}, {self.adress}, {self.email}, {self.birthday}, {self.age}'

adressbook1=AddressBook('1','Petro','1234567','lviv','qwerty123@gmail.com','01.01.91','45')
print(AddressBook('1','Petro','1234567','lviv','qwerty123@gmail.com','01.01.91','45'))
#9
class Person:
    name = 'John'
    age = '36'
    country='USA'
setattr(Person, 'age', '46')

John1 = Person()
print(getattr(John1, 'age'))

#10
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

student=Student(10,'Andriy')

setattr(student,"id", "0")
print(getattr(student,"id",'0'))

setattr(student,"name", "Vasyl")
print(getattr(student,"name", "Vasyl"))

setattr(student,"email", "asdfg@gmail.com")
print(getattr(student,"email", "asdfg@gmail.com"))



