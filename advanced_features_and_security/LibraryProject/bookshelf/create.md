\# Create Book



```python

from bookshelf.models import Book



\# Create a book instance

book = Book.objects.create(

&nbsp;   title='1984',

&nbsp;   author='George Orwell',

&nbsp;   publication\_year=1949

)

book

\# Output: <Book: 1984>

