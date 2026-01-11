
---

# **2️⃣ retrieve.md**

```markdown
# Retrieve Book

```python
from bookshelf.models import Book

# Retrieve all books
Book.objects.all()

# Retrieve a specific book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
