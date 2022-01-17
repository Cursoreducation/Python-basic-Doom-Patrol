import os


def file_rename(filename):
    def rename_decorator(func):
        def inner():
            old_filename = func()
            os.rename(old_filename, filename)

        return inner

    return rename_decorator


@file_rename('hello.txt')
def create_file():
    file_name = "copy.txt"
    file = open(file_name, "w")
    file.write("Your text goes here")
    file.close()
    return file_name

create_file()