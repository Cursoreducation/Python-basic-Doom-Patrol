def tag(tag_name):
    def tag_decorator(func):
        def wrapper(*args):
            return f"<{tag_name}>{func(args[0])}</{tag_name}>"

        return wrapper

    return tag_decorator


@tag('b')
def get_text(name):
    return f"Hello {name}"

print(get_text('Rostyslav'))