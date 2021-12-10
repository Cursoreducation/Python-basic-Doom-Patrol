from collections import namedtuple
import dataclasses

# 1.
# class Laptop:
#     """
#     Make the class with composition.
#     """
# class Battery:
#     """
#     Make the class with composition.
#     """


class Laptop:
    def __init__(self, brand, battery_name):
        self.brand = brand
        self.battery_name = battery_name
        self.working_hrs = Battery().get_hrs(battery_name)

    def get_working_hrs(self):
        btr_obj = Battery()
        return btr_obj.get_hrs(self.battery_name)


class Battery:
    accumulators = {'hwd2020': 8, 'olion17': 12}

    def get_hrs(self, battery_type):
        return self.accumulators[battery_type]


hp = Laptop('HP', 'hwd2020')
asus = Laptop('ASUS', 'olion17')
print(hp.get_working_hrs())
print(asus.working_hrs)

# 2.
# class Guitar:
#     """
#     Make the class with aggregation
#     """
# class GuitarString:
#     """
#     Make the class with aggregation
#     """


class Guitar:
    def __init__(self, name, string_count):
        self.name = name
        self.string_count = string_count

    def display(self):
        print(self.name)
        print(gs.display())


class GuitarString:
    def __init__(self, string_count):
        self.string_count = string_count

    def display(self):
        return self.string_count


gs = GuitarString(8)
myGuitar = Guitar("roxy", gs)
myGuitar.display()

# 3 class Calc:
#    Make class with one method "add_nums" with 3 parameters,
#    which returns sum of these parameters.
#    Note: this method should be static


class Calc:

    @staticmethod
    def add_params(arg1, arg2, arg3):
        return arg1 + arg2 + arg3


print(Calc.add_params(2, 5, 1))

# 4*.
# class Pasta:
#     Make class which takes 1 parameter on init - list of ingredients
#     and defines instance attribute ingredients.
#     It should have 2 methods:
#     carbonara (['forcemeat', 'tomatoes']) and
#     bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']


class Pasta:
    carbonara_ingrts = ['forcemeat', 'tomatoes']
    bolognaise_ingrts = ['bacon', 'parmesan', 'eggs', 'cucumber']
    type = ('carbonara', 'bolognaise')

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return cls(cls.type[0], cls.carbonara_ingrts)

    @classmethod
    def bolognaise(cls):
        return cls(cls.type[1], cls.bolognaise_ingrts)


pasta_1 = Pasta('carbonara', ["tomato", "cucumber"])
print(pasta_1.ingredients)
pasta_2 = Pasta.bolognaise()
print(pasta_2.ingredients)


# 5.
# Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
# In case of setting visitors_count - max_visitors_num should be checked,
# if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
# Example:
#     Concert.max_visitor_num = 50
#     concert = Concert()
#     concert.visitors_count = 1000
#     print(concert.visitors_count)  # 50


class Concert:
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self._visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, count):
        self._visitors_count = count if count <= self.max_visitors_num else \
            self.max_visitors_num


Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)

# 6.
# class AddressBookDataClass:
#     Create dataclass with 7 fields - key (int), name (str),
#     phone_number (str), address (str), email (str), birthday (str), age (int)


@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


address_list = AddressBookDataClass(key=5,
                                    name='Harry',
                                    phone_number='25-58-89',
                                    address='opop str 2',
                                    email='fest@fo.com',
                                    birthday='123456',
                                    age=18)
print(address_list.name)

# 7. Create the same class (6) but using NamedTuple

AddressBookTuple = namedtuple('AddressBookDataClass', ['key',
                                                       'name',
                                                       'phone_number',
                                                       'address',
                                                       'email',
                                                       'birthday',
                                                       'age'])

address_tuple = AddressBookTuple('1', 'o', '1', 'aa', 'r@t', '23456', 8)
print(address_tuple.name)

# 8.
# class AddressBook:
#     Create regular class taking 7 params on init -
#     key, name, phone_number, address, email, birthday, age
#     Make its str() representation the same as for
#     AddressBookDataClass defined above.
#     Expected result by printing instance of AddressBook:
#     AddressBook(key='', name='', phone_number='', address='', email='',
#     birthday= '', age='')


class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __repr__(self):
        return(f'AddressBook(key={self.key}, name={self.name}, '
               f'phone_number={self.phone_number}, address={self.address},'
               f'email={self.email}, birthday={self.birthday}, '
               f'age={self.age})')


address_book = AddressBook("0", "w", "p", "i", "ds", "sd", "s")
print(address_book)

# 9.
# class Person:
#     Change the value of the age property of the person object


class Person:
    name = "John"
    age = 36
    country = "USA"


my_person = Person()
setattr(my_person, 'age', 28)
print(my_person.age)

# 10.


class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' var and print it using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


my_student = Student(1245, "Alex")
setattr(my_student, 'email', 'bla@i.o')

# 11*.


class Celsius:
    """
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
    """
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, new_temperature):
        self._temperature = new_temperature


f_temp = Celsius(12)
f_temp.temperature = (f_temp.temperature * 1.8) + 32
print(f_temp.temperature)
