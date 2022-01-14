def pow_it(a):
    return a ** 2


def my_decorator(func):
    def inner():
        print('Print before function')
        a = func()
        print(f'Print after function: {pow_it(a)}')

    return inner


@my_decorator
def foo():
    return 10


# foo = my_decorator(foo)
foo()
