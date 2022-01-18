import time
from datetime import datetime


class Logger:
    logfile = 'out.log'

    def __init__(self, func_to_decorate):
        self.func_to_decorate = func_to_decorate

    def __call__(self):
        log = f'{self.func_to_decorate.__name__} was executed at {datetime.now()}\n'
        print(log)
        with open(self.logfile, 'a') as file:
            file.write(log)


@Logger
def my_func():
    """
    This is my func
    """
    print(f"{my_func().__name__} is running")


my_func()
