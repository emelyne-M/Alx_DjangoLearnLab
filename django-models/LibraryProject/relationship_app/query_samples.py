
from relationship_app.models import Author, Book, Library, Librarian

# 1️⃣ Query all books by a specific author
def books_by_author(author_name):
   
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return Book.objects.none()  # returns empty queryset if author doesn't exist

# 2️⃣ List all books in a library
def books_in_library(library_name):
   
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return Book.objects.none()  # returns empty queryset if library doesn't exist

# 3️⃣ Retrieve the librarian for a library
def librarian_for_library(library_name):
   
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian  # will be None if no librarian assigned
    except Library.DoesNotExist:
        return None
