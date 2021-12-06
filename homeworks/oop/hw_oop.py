# 1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


my_vehicle = Vehicle(140, 200)
print(my_vehicle)

# 2. Create a child class Bus that will inherit all the variables and
#    methods of the Vehicle class and will have seating_capacity own method

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seat_capacity):
        Vehicle.__init__(self, max_speed, mileage)
        self.seat_capacity = seat_capacity

    def seating_capacity(self):
        self.seat_capacity = input('Input count of seats: ')

my_bus = Bus(90, 300, 20)

# 3. Determine which class a given Bus object belongs to (Check type of an object)
print(type(my_bus))
print(isinstance(my_bus, Vehicle))

# 4. Create an instance of Bus named school_bus and determine if school_bus is also an instance of the Vehicle class
school_bus = Bus(80, 200, 30)
print(isinstance(school_bus, Vehicle))

# 5. Create a new class School with get_school_id and number_of_students instance attributes
class School:
    def __init__(self, school_id, number_of_students):
        self.school_id = school_id
        self.number_of_students = number_of_students

    def get_school_id(self):
        return self.school_id

# 6*. Create a new class SchoolBus that will inherit all the methods from School
#     and Bus and will have its own - bus_school_color
class SchoolBus(School,Bus):
    def __init__(self, school_id, number_of_students, max_speed, mileage, seat_capacity, bus_school_color):
        School.__init__(self, school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seat_capacity)
        self.bus_school_color = bus_school_color

my_schoolBus = SchoolBus(25, 300, 60, 110, 30, "yellow")
print(my_schoolBus.bus_school_color)

# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,
#    make a tuple of it and by using for call their action using the same method.
class Bear:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        return ("Bear says " + self.sound)

class Wolf:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        return ("Wolf says " + self.sound)

bear = Bear("Grr")
wolf = Wolf("Ayy")

wild_animals = (bear, wolf)
for animal in wild_animals:
    print(animal.make_sound())

#    Magic methods:
# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
#    otherwise return message: "Your city is too small".
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def get_population(self):
        if self.population < 1500:
            return "Your city is too small"
        return self.population


tokyo = City("Tokyo", 37435191)
delhi = City("Delhi", 29399141)
pidkovka = City("Pidkovka", 800)

cities = (tokyo, delhi, pidkovka)

for i in cities:
    print(i.get_population())

