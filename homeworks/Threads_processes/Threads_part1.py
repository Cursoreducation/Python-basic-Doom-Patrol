import threading
# 1. Write the method that returns the number of threads currently in execution
# Also, prepare the method that will be executed with threads and run during
# the first method counting.
# (multithreading)


def get_threads_count():
    return threading.active_count()


def say_hello(num, name):
    for _ in range(num):
        print(f"Hello {name}", "\n")


t1 = threading.Thread(target=say_hello, args=[5, 't1', ])
t2 = threading.Thread(target=say_hello, args=[2, 't2', ])

say_hello(5, 'main')
print(f'Active threads count before start: {get_threads_count()}')

t1.start()
t2.start()

print(f'Active threads count before join: {get_threads_count()}')

t1.join()
t2.join()

print(f'Active threads count: {get_threads_count()}')