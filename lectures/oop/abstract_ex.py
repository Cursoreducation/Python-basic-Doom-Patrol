# from abc import abstractmethod, ABC
#
#
# class Greetings(ABC):
#
#     @abstractmethod
#     def say_hello(self):
#         raise NotImplementedError
#
#     @abstractmethod
#     def say_hi(self):
#         raise NotImplementedError
#
#     @abstractmethod
#     def say_great(self):
#         raise NotImplementedError
#
#
# class Ukraine(Greetings):
#     def say_hello(self):
#         print('Доброго дня')
#
#     def say_hi(self):
#         print('Привіт')
#
#     def say_great(self):
#         pass
#
#
# class English(Greetings):
#     def say_hello(self):
#         print('Hello')
#
#     def say_hi(self):
#         print('Hi')
#
#     def say_great(self):
#         pass
#
#
# class Spain(Greetings):
#     def say_hello(self):
#         print('Hola')
#
#     def say_hi(self):
#         pass
#
#     def say_great(self):
#         pass
#
#
# if __name__ == "__main__":
#     ukr = Ukraine()
#     eng = English()
#     sp = Spain()
#     ukr.say_hello()
#     ukr.say_hi()
#     eng.say_hello()
#     eng.say_hi()

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def do(self, action):
        pass


class Lion(Animal):
    def do(self, a, b):
        print(f"{a} {b} a lion!")


class Panda(Animal):
    def do(self, action):
        print(f"{action} a panda!")

lion = Lion()
lion.do('a', 'b')