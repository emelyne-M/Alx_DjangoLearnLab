from rest_framework import generics, permissions,filters
from .models import Book
from .serializers import BookSerializer

# Read-only views

class BookListView(generics.ListAPIView):
    
    """
    GET /api/books/
    List all books in the database.
    Accessible by anyone (public view).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['publication_year', 'title']


class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<id>/
    Retrieve a single book by its ID.
    Accessible by anyone (public view).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Authenticated CRUD views
class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Create a new book.
    Only accessible by authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /api/books/<id>/update/
    Update an existing book by ID.
    Only accessible by authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/<id>/delete/
    Delete a book by ID.
    Only accessible by authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
