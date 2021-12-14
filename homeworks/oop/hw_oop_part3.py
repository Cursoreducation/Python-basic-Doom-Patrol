import time
import random
import uuid
from abc import ABC, abstractmethod


class Animal(ABC):  # common attributes and methods of Herbivores, Predator
    types = ("Herbivores", "Predator")

    def __init__(self, power, speed):
        self.id = uuid.uuid4()
        self.max_power = power
        self.current_power = power
        self.speed = speed
        self.is_out_of_power = False

    def eat(self, power):
        self.current_power += power \
            if self.current_power + power <= self.max_power else self.max_power

    def waist_power(self, power):
        self.current_power -= power
        if self.current_power <= 0:
            self.is_out_of_power = True

    @abstractmethod
    def get_name(self):
        pass

    def get_animal_info(self):
        return self.get_name() + "\t" + str(self.id)


class Predator(Animal):
    def get_name(self):
        return self.types[1]  # returns Predator


class Herbivorous(Animal):
    def get_name(self):
        return self.types[0]  # returns Herbivorous


class Forest:
    # class Forest contains dictionary of animals in format{uniq_id:Animal()}
    def __init__(self):
        self.animals = dict()

    def add_animal(self, animal):  # add Animal() to Forest
        self.animals[animal.id] = animal

    def remove_animal(self, animal):  # delete Animal() from Forest
        del self.animals[animal.id]

    def get_animals_count(self):  # get count of animals in Forest
        return len(self.animals)

    @property
    def is_hunting_possible(self):  #
        """
            hunting is possible if there is at least one animal in forest
        """
        # the Forest at least one Animal
        if self.get_animals_count() <= 1:  # it's 1 or 0 animal - stop hunting
            return False
        return True

    def get_animal(self, hunter_id=None):
        """
            returns randomly chosen hunter(if hunter_id = None) or victim
            hunter_id: uniq id of animal which is already selected as hunter. used to select a victim
        """
        if not isinstance(hunter_id, type(None)):
            key_list = list(key for key in self.animals.keys()
                            if key != hunter_id)
        else:
            key_list = list(self.animals.keys())

        animal_key = random.choice(key_list)
        return self.animals[animal_key]

    @staticmethod
    def print_animal_list():
        """
            prints info = name , id  for all animals in forest
        """
        for animal in my_forest.animals.keys():
            print(my_forest.animals[animal].get_animal_info())

    def any_predator_left(self):
        """
            return true if there is any predator in forest
        """
        for key in self.animals.keys():
            if isinstance(self.animals[key], Predator):
                return True

        return False

    def start_hunting(self):
        """
            Randomly chosen hunter is checked to be a herbivorous animal.
            If so then no need to hunt, just eating and restoring its power.
            In other case it starts hunting process. Randomly chosen victim
            could be either herbivorous or predator animal.
            If hunter's speed and power is greater than victim's he will eat
            his victim - hunter's power +50%, victim is removed from forest.
            Other way power of both victim and hunter is reduced by 30%
            If power of animal is less equal 0 we assume it as dead and remove
            from forest
        """
        hunter = Forest.get_animal(self)

        if isinstance(hunter, Herbivorous):  # Herbivorous, eating => power +50
            hunter.eat(50)

        # hunter is Predator, try to catch up some victim
        victim = Forest.get_animal(self, hunter.id)  # randomly choose victim

        if hunter.speed > victim.speed and \
                hunter.current_power > victim.current_power:
            hunter.eat(50)  # hunter's power +50% , victim - dead
            victim.is_out_of_power = True
        else:
            hunter.waist_power(30)  # the victim managed to survive
            victim.waist_power(30)  # both -30% of power

        # checking who's out of power and get rid of such animal
        if hunter.is_out_of_power:
            self.remove_animal(hunter)

        if victim.is_out_of_power:
            self.remove_animal(victim)


class AnimalGenerator:
    # returns randomly created instance of Predator or Herbivorous class
    def __iter__(self):
        return self

    def __next__(self):
        animal_type = random.choice(Animal.types)  # Predator or Herbivorous

        if animal_type == "Predator":
            new_animal = Predator(random.randint(25, 100),
                                  random.randint(25, 100))
        else:
            new_animal = Herbivorous(random.randint(25, 100),
                                     random.randint(25, 100))

        return new_animal


if __name__ == "__main__":

    nature = AnimalGenerator()
    my_forest = Forest()

    for i in range(10):
        animal = next(nature)
        my_forest.add_animal(animal)

    print("Who leaves in the forest?")
    my_forest.print_animal_list()

    print("Ready... Steady... Go hunting!")

    time.sleep(3)

    while my_forest.any_predator_left() and my_forest.is_hunting_possible:
        my_forest.start_hunting()

    print("Has anyone survived? Lets have a look...")
    my_forest.print_animal_list()

