class TestClass:
    def instance_method(self):
        print(f'Called instance_method of {self}')

    @classmethod
    def class_method(cls):
        print(f'Called class_method of {cls}')

    @staticmethod
    def static_method():
        print('Called static_method')

test = TestClass()
test.instance_method()
TestClass.instance_method(test)

TestClass.class_method()
TestClass.static_method()

class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f'Book {self.name}, {self.book_type}, {self.weight}'


    @classmethod
    def hardcover(cls, name, weight):
        # return Book(name, Book.TYPES[0], weight + 50)
        return cls(name, cls.TYPES[0], weight + 50)

    @classmethod
    def paperback(cls, name, weight):
        return cls(name, cls.TYPES[1], weight)


book_1 = Book.hardcover('Kobzar', 1000) #Book('Kobzar', 'hardcover', 1000)
book_2 = Book.paperback('Book', 500)
print(book_1)
print(book_2)