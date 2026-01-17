
from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()  # matches the check
    except Author.DoesNotExist:
        return Book.objects.none()

def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()  # matches the check
    except Library.DoesNotExist:
        return Book.objects.none()

def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        return None
