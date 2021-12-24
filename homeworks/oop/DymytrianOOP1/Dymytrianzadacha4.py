#1Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:

    def __init__(self, maxspeed, mileage, capasyty):
        self.maxspeed=maxspeed
        self.mileage=mileage
        self.capasyty=capasyty


#2Create a child class Bus that will inherit all the variables and methods of the Vehicle class and will have seating_capacity own method

class Buss(Vehicle):

    def seat_capacity (self):
        print (f'capasyty: {self.capasyty}')
#3Determine which class a given Bus object belongs to (Check type of an object)

School_Buss=Buss(160,200000,200)
print(type(School_Buss))

#4Determine if School_bus is also an instance of the Vehicle class

print(isinstance(School_Buss,Vehicle))

#5Create a new class School with get_school_id and number_of_students instance attributes

class School:
    def __init__(self, school_id, number_of_students):
        self.school_id = school_id
        self.number_of_students = number_of_students

    def print_number_of_students(self):
        print('We a have next', {self.number_of_students})
    def get_school_id(self):
        print("Id number school ", {self.school_id})

#7Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,
#make a tuple of it and by using for call their action using the same method.

class Volf:

    def __init__(self,sound):
        self.sound=sound
    def make_sound (self):
        print("Volf sound:",self.sound)


Volf1=Volf("UUUUU")
Volf1.make_sound()

class Bear:

    def __init__(self,sound):
        self.sound=sound
    def make_sound (self):
        print("Bear sound:",self.sound)


Bear1=Bear("EEEEE")
Bear1.make_sound()

predators=tuple([Volf1,Bear1])

for predators in predators:
    print( predators.make_sound())

















