
# api/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework     
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer

# ---------------------------
# READ-ONLY VIEWS
# ---------------------------
class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    List all books with filtering, searching, ordering.
    Permissions: anyone can view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'publication_year', 'author__name']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ---------------------------
# AUTHENTICATED CRUD VIEWS
# ---------------------------
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
