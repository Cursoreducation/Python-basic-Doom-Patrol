class WrongFactorialNumber(Exception):
    def __init__(self, num, message=' - wrong number to calculate factorial'):
        self.num = num
        self.message = message

    def __str__(self):
        return f'{self.num} {self.message}'


def number_verification(func):
    def inner(num):
        if isinstance(num, int) and num > 0:
            return func(num)
        else:
            print(f'Your number: {num}, You have to use only positive and integer')

    return inner


@number_verification
def factorial(n):
    # Checking the number
    # is 1 or 0 then
    # return 1
    # otherwise return
    # factorial
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


lst = [1, 2, 5, '2', -1, 0, 2.3]

for i in lst:
    factorial(i)
