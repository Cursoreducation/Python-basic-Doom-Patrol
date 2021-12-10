from random import random
def simple_generator(val):
    while val > 0:
        val -= 1
        if val == 3:
            return val
        yield val


# gen = simple_generator(5)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

def random_num_increaser(quantity):
    start = 0
    while quantity > 0:
        start += random()
        quantity -= 1
        yield round(start, 1)

# gener = random_num_increaser(5)
# for i in gener:
#     print(i)

g = (round(random()+i, 1) for i in range(5))
print(dir(g))
for i in g:
    print(i)