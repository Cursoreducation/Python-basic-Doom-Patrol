
def smart_divide(func):
    def inner(a, b):
        print(f'I am going to divide {a} by {b}')
        if b == 0:
            print('Whoop, I am not able to divide by 0')
            return False
        else:
            result = func(a, b)
            return result

    return inner

# def smart_divide(func):
#     def inner(*args, **kwargs):
#         a = args[0]
#         b = args[1]
#         print(f'I am going to divide {a} by {b}')
#         if b == 0:
#             print('Whoop, I am not able to divide by 0')
#             return False
#         else:
#             result = func(a, b)
#             return result
#
#     return inner

@smart_divide
def divide(a, b):
    return a / b



print(divide(1, 0, test='test'))
