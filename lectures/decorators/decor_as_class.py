# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print('Before func()')
#         self.func()
#         print('After func()')

class MyDecorator:
    def __init__(self, func, a, b):
        self.func = func
        self.a = a
        self.b = b

    def __call__(self, *args, **kwargs):
        print(f'Before func(): {args[0]}')
        self.func(args[0], kwargs["test"])
        print(f'After func(): {kwargs["test"]}')


@MyDecorator(a=2, b=3)
def foo(a, b):
    print('Test')

foo(1, test=2)
