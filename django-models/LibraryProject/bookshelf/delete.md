
---

# **4️⃣ delete.md**

```markdown
# Delete Book

```python
from bookshelf.models import Book

# Get the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete it
book.delete()

# Verify deletion
Book.objects.all()
