
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

# ------------------------
# READ-ONLY VIEWS
# ------------------------
class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    List all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # ALX wants this
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['publication_year', 'title']


class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<id>/
    Retrieve a single book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# ------------------------
# AUTHENTICATED CRUD VIEWS
# ------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
