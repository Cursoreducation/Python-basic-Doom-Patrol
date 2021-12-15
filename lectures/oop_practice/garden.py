# # **Garden**
# We have only one garden. In the garden can have vegetables, fruits and pests.
# Each fruit or vegetable should have a stage of maturity (stages: None, Flowering, Green, Red).
# Pests can eat only green and red fruit or vegetable. Once pests eat the fruit, it should be removed.

# ## There is a Tomato with the following characteristics:
# 1. Number of tomatoes (Index)
# 2. Vegetable type

# ### A tomato can:
# 1. Grow (move to the next stage of maturation)
# 2. Provide information about your maturity

# ### There is a Tomato Bush that:
# 1. Contains a list of tomatoes that grow on it

# ### And:
# 1. Grow with tomatoes
# 2. Provide information on the maturity of all tomatoes
# 3. Provide harvest

# ## There is an Apple with the following characteristics:
# 1. Number of apples (Index)
# 2. Fruit type

# ### An apple can:
# 1. Grow (move to the next stage of maturation)
# 2. Provide information about your maturity

# ### There is an Apple Tree that:
# 1. Contains a list of apples that grow on it

# ### And:
# 1. Grow with apples
# 2. Provide information on the maturity of all apples
# 3. Provide harvest

# ## And there is also a Gardener who has:
# 1. Name
# 2. The plants he looks after

# ### And:
# 1. Take care of the plant
# 2. Poison the pests
# 2. Harvest from it

# ## And there is also a Pests who have:
# 1. Type
# 2. Quantity


# ## And:
# 1. Eat the plants
from abc import ABC, abstractmethod

stages = {0: 'None', 1: 'Flowering', 2: 'Green', 3: 'Red'}


class GardenMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMeta):
    def __init__(self, vegetables, fruits, pests):
        self.vegetables = vegetables
        self.fruits = fruits
        self.pests = pests

    def show_the_garden(self):
        print(f"I have {self.vegetables} and {self.fruits} and {self.pests}")


class Vegetables(ABC):

    @abstractmethod
    def grow(self):
        pass

    @abstractmethod
    def is_ripe(self):
        pass


class Fruits(ABC):

    @abstractmethod
    def grow(self):
        pass

    @abstractmethod
    def is_ripe(self):
        pass


class Tomato(Vegetables):
    def __init__(self, tomatoes_index, vegetable_type):
        self.tomatoes_index = tomatoes_index
        self.vegetable_type = vegetable_type
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.grow_info()

    def is_ripe(self):
        return self.state == 3

    def grow_info(self):
        print(f'{self.vegetable_type} - {self.tomatoes_index}: {stages[self.state]}')


class TomatoBush:
    def __init__(self, number_of_tomatos):
        self.all_tomatoes = [Tomato('Cherry', index) for index in range(number_of_tomatos)]

    def grow_all(self):
        for tomato in self.all_tomatoes:
            tomato.grow()

    def is_ripe_all(self):
        return all([tomato.is_ripe() for tomato in self.all_tomatoes])

    def harvest(self):
        self.all_tomatoes = []


class Apple(Fruits):
    def __init__(self, apple_index, fruit_type):
        self.apple_index = apple_index
        self.fruit_type = fruit_type
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.grow_info()

    def is_ripe(self):
        return self.state == 3

    def grow_info(self):
        print(f'{self.fruit_type} - {self.apple_index}: {stages[self.state]}')


class AppleTree:
    def __init__(self, number_of_apple):
        self.all_apples = [Apple('White', index) for index in range(number_of_apple)]

    def grow_all(self):
        for apple in self.all_apples:
            apple.grow()

    def is_ripe_all(self):
        return all([apple.is_ripe() for apple in self.all_apples])

    def harvest(self):
        self.all_apples = []


class Gardener:
    def __init__(self, name, plants_list):
        self.name = name
        self.plants_list = plants_list

    def take_care(self):
        print("watering the plants")
        for plant in self.plants_list:
            plant.grow_all()

    def harvest(self):
        for plant in self.plants_list:
            if plant.is_ripe_all:
                print('Harvesting...')
                plant.harvest()
            else:
                print("It's not ready for harvest")


# class Pests:
#     def __init__(self, pests_type, pests_quantity, plants)
#
#     def eat_plants():
#         for plant in plants:
#             if


apple_tree = AppleTree(3)
tomato_bush = TomatoBush(4)
print(tomato_bush.all_tomatoes)
print(apple_tree.all_apples)

gardener = Gardener("Homer", [apple_tree, tomato_bush])
for _ in range(3):
    gardener.take_care()
gardener.harvest()
print(tomato_bush.all_tomatoes)
print(apple_tree.all_apples)
