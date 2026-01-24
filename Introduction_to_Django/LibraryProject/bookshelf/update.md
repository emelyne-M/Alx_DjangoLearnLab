
---

# **3️⃣ update.md**

```markdown
# Update Book

```python
from bookshelf.models import Book

# Get the book
book = Book.objects.get(title="1984")

# Update title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
book.title
