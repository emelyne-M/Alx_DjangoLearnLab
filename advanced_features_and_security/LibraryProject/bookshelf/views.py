from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_protect
from .models import Book
from .forms import BookForm

# ==============================
# List all books (view permission)
# ==============================
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})


# ==============================
# Create a new book (create permission)
# ==============================
@permission_required('bookshelf.can_create', raise_exception=True)
@csrf_protect
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Safe ORM call
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})


# ==============================
# Edit an existing book (edit permission)
# ==============================
@permission_required('bookshelf.can_edit', raise_exception=True)
@csrf_protect
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()  # Safe ORM call
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/form_example.html', {'form': form})


# ==============================
# Delete a book (delete permission)
# ==============================
@permission_required('bookshelf.can_delete', raise_exception=True)
@csrf_protect
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/confirm_delete.html', {'book': book})


# ==============================
# Search books (safe ORM query)
# ==============================
@permission_required('bookshelf.can_view', raise_exception=True)
def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)  # Safe query
    return render(request, 'bookshelf/list_books.html', {'books': books})

