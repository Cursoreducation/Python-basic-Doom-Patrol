import time


def timer(func):
    def inner():
        start = time.time()
        res = func()
        result = time.time() - start
        return res, result

    return inner


@timer
def calculate():
    time.sleep(2)
    return 'Hi there'


# result, time_result = calculate()
# print(result)
# print(time_result)


def logger(func):
    def inner(*args):
        print(f'Call the function: {func.__name__}')
        result = func(*args)
        print(result)
        print(f'End of fuction call: {func.__name__}')
        return result
    return inner

@logger
def calculate():
    time.sleep(2)
    return 'Hi there'

calculate()