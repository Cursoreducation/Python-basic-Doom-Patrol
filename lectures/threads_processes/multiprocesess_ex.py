import time
from multiprocessing import Process
import os

def foo():
    print('calling foo')
    print(f'parent process id: {os.getppid()}')
    print(f'process id: {os.getpid()}')
    time.sleep(30)

def main():
    print('calling main')
    p = Process(name='Service 1', target=foo)
    p.start()
    print(f'Process p is alive: {p.is_alive()}')
    p.join()


if __name__ == '__main__':
    main()