from collections import namedtuple

Article = namedtuple('Article', ['topic', 'pages', 'language', 'author'])

python_programming = Article('Python Programming styles', 14, 'EN', 'Rostyslav')
print(python_programming)
print(python_programming.pages)
