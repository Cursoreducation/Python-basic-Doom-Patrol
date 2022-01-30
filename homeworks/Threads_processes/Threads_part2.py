import multiprocessing
from math import sqrt
# 2. Write a program that will calculate two quadratic equations
# (6x² + 11x - 35 = 0. and 5x² - 2x - 9 = 0.) at the same time,
# set all the parameters of the equation in variables. (multiprocessing)


def calc_equation(coefficients):
    a = coefficients[0]
    b = coefficients[1]
    c = coefficients[2]
    d = b ** 2 - 4 * a * c
    roots = lambda a, b: {(-b - sqrt(d)) / (2 * a), (-b + sqrt(d)) / (2 * a)} \
        if d >= 0 else {}
    print(roots(a, b))


coefficients1 = multiprocessing.Array('i', (6, 11, -35))
coefficients2 = multiprocessing.Array('i', (5, -2, -9))
p1 = multiprocessing.Process(target=calc_equation, args=(coefficients1,))
p2 = multiprocessing.Process(target=calc_equation, args=(coefficients2,))

p1.start()
p2.start()

p1.join()
p2.join()





