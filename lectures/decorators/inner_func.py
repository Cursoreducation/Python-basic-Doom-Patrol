def parent():
    print('Print from the parent() function')
    foo = 'Hello'

    def first_child():
        print(f'Printing from the first_child() function: {foo}')

    def second_child():
        print(f'Printing from the second_child() function {foo}')

    first_child()
    second_child()


def calculate_smth(a, b):
    c = a + b * (b + a)

    def pow_it(c):
        return c ** 2

    c = pow_it(c)
    return pow_it

calculate_smth(5, 7)
