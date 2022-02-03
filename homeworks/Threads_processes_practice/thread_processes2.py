import glob
import threading
import time
from queue import Queue


# 2. Resolve the second (2b.) task from practice With multithreading
# Create a script that should find the line that you provided to it
# in the provided directory.


def find_by_pattern(q, pattern):
    container = []
    while not q.empty():
        with open(q.get()) as file:
            for line in file:
                if pattern in line:
                    container.append(line)
        q.task_done()
    return container


def find_all_files(directory_path, pattern, q_res):
    files = glob.glob(f'{directory_path}/*.py')

    for file in files:
        q.put(file)

    q_res.put(find_by_pattern(q, pattern))


if __name__ == '__main__':
    q = Queue()
    q_result = Queue()
    start = time.time()

    first = threading.Thread(target=find_all_files,
                             args=['.', 'ThreadPoolExecutor', q_result])
    second = threading.Thread(target=find_all_files,
                              args=['.', 'ProcessPoolExecutor', q_result])
    third = threading.Thread(target=find_all_files,
                             args=['.', 'get_session', q_result])
    fourth = threading.Thread(target=find_all_files,
                              args=['.', 'result.text', q_result])
    fifth = threading.Thread(target=find_all_files,
                             args=['../threads_processes', 'ThreadPoolExecutor',
                                   q_result])
    sixth = threading.Thread(target=find_all_files,
                             args=['../threads_processes', 'ProcessPoolExecutor',
                                   q_result])
    seventh = threading.Thread(target=find_all_files,
                               args=['../threads_processes', 'get_session',
                                     q_result])
    eighth = threading.Thread(target=find_all_files,
                              args=['../threads_processes', 'result.text',
                                    q_result])

    first.start()
    second.start()
    third.start()
    fourth.start()
    fifth.start()
    sixth.start()
    seventh.start()
    eighth.start()

    first.join()
    second.join()
    third.join()
    fourth.join()
    fifth.join()
    sixth.join()
    seventh.join()
    eighth.join()

    print(f'Total time for search: {time.time() - start}')

    while not q_result.empty():
        print(q_result.get())
