from django.shortcuts import render
from bookshelf.models import Book
from .models import Library
from django.views.generic.detail import DetailView 

# Function-based view
def list_books(request):
    books = Book.objects.all()  # required by checker
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
