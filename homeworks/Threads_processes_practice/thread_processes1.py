import glob
import os
import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

from pathlib import Path

#1. Create a script that should find the lines by provided pattern in
# the provided path directory with recursion* and threads. *(it means
# if the directory has other directories, the script should get all the info
# from them as well)

SEARCH_USER = "user"
SEARCH_EMAIL = "email"

RESULT_USER = 'user.txt'
RESULT_EMAIL = 'email.txt'


def find_by_pattern(pattern):
    lines_container = []
    path = "../**/*.txt"
    for filename in glob.iglob(path, recursive=True):
        with open(filename) as file:
            for line in file:
                if pattern in line:
                    lines_container.append(line)

    return lines_container


def write_to_file(lines_container, file_name):
    file = open(file_name, 'w')
    file.writelines(lines_container)
    file.close()


if __name__ == '__main__':
    start = time.time()
    with ThreadPoolExecutor(max_workers=2) as pool:
        pool.submit(write_to_file(find_by_pattern(SEARCH_USER), RESULT_USER))
        pool.submit(write_to_file(find_by_pattern(SEARCH_EMAIL), RESULT_EMAIL))
    stop = time.time() - start
    print(stop)





