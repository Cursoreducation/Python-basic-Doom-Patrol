from functools import wraps


def logger(func):
    @wraps(func)
    def inner(*args, **kwargs):
        """
        Inner func
        :param args:
        :param kwargs:
        :return:
        """
        print(f'{func.__name__} was called')
        return func(*args, **kwargs)

    return inner


@logger
def foo(x):
    """
    Foo func
    :param x:
    :return:
    """
    return x + x * x


print(foo(5))

print(foo.__name__)
print(foo.__doc__)
