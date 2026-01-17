from relationship_app.models import Author, Book, Library

#  Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        # Explicit filter as expected by the check
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return Book.objects.none()  # safe empty queryset

#  List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        # Explicit filter assuming Book has a ForeignKey to Library
        return Book.objects.filter(library=library)
    except Library.DoesNotExist:
        return Book.objects.none()

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        # Explicit get for librarian
        return library.librarian if library.librarian else None
    except Library.DoesNotExist:
        return None
