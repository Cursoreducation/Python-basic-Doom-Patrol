from global_defines import *


def add(x, y):
    return convert_to_str_line(x, y, x + y)


def subtract(x, y):
    return convert_to_str_line(x, y, x - y)


def multiply(x, y):
    return convert_to_str_line(x, y, x * y)


def divide(x, y):
    if y == 0:
        return convert_to_str_line(x, y, "Ho ho ho, don't break me")
    return convert_to_str_line(x, y, x / y)


def power_by(x, y):
    return convert_to_str_line(x, y, x ** y)


def convert_to_str_line(x, y, res):
    """
    Returns formatted string for writing it to file
    :param x:  1
    :param y:  1
    :param res: 2
    :return: 1 + 1 = 2
    """

    frame = inspect.currentframe()
    call_frame = inspect.getouterframes(frame, 2)
    call_func = (call_frame[1][3]).lower()

    return f'{x} {operations[call_func]} {y} = {res}'


def write_to_file(path, text):
    """
        adds text string to file
    """
    with open(path, 'a') as wfile:
        wfile.write("\n" + text)


def clear_file(path):
    """
        if file or directory from path param doesn't exist then it creates it,
        also it will clear file if it already exists
        adds current date and time as first line
    """

    path_to_file = path.rpartition("/")[0]
    if not os.path.exists(path_to_file):
        os.makedirs(path_to_file)

    with open(path, 'w') as file:
        file.write(str(datetime.now()))
