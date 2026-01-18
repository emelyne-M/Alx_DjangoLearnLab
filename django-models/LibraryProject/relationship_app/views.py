from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from bookshelf.models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Function-based view for user registration
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()       # Save the new user
            login(request, user)     # Automatically log them in
            return redirect('list_books')  # Redirect after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
