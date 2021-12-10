# d = [1, 2, 3, 4]
# s = 'cat'
# l = {'key': 'value'}
# i = {1, 2, 3}
# # print(dir(d))
#
# for k in d:
#     print(k)
#
# test = iter(d)
# print(test)
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# try:
#     print(next(test))
# except StopIteration:
#     pass

# class Iterable:
#     number = 0
#
#     def __getitem__(self, item):
#         self.number += 1
#         if self.number == 10:
#             raise StopIteration
#         return self.number
#
# iterable = Iterable()
# for k in iterable:
#     print(k)

# __iter__() __next__()
from random import random


class RandomNumIncreaser:
    def __init__(self, quantity):
        self.quantity = quantity
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.quantity > 0:
            self.start += random()
            self.quantity -= 1
            return round(self.start, 1)
        else:
            raise StopIteration


it = RandomNumIncreaser(5)
# for i in it:
#     print(i)


def check_if_object_is_iterable(obj):
    return '__getitem__' in dir(obj)


types_to_check = [int, bool, str, float, list, tuple, dict, set, bytes, bytearray, range(1)]
for item in types_to_check:
    print(f'{item} Iterable - {check_if_object_is_iterable(item)}')
