import dataclasses


@dataclasses.dataclass
class Article:
    topic: str
    contributor: str
    language: str
    upvotes: int
    pages: int


python_programming = Article(topic='Python Programming styles',
                             contributor='Rostyslav',
                             language='EN',
                             upvotes='5',
                             pages=14)


print(python_programming)
print(python_programming.pages)
print(python_programming.topic)
python_programming.pages = 15
python_programming.new_attr = 'hello'
print(python_programming.new_attr)


@dataclasses.dataclass(frozen=True)
class Book:
    title: str
    author: str
    pages: int


book = Book('Harry Pother', 'J.K.Rougling', 578)

print(book.title)
# book.likes = '1kkkk'

dct = {
    "title": 'Harry Pother',
    'author': 'J.K.Rougling',
    'pages': 578
}

print(dct['title'])
print(dct.get('title'))
