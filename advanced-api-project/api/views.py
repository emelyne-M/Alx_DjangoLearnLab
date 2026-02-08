from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer

# ------------------------
# READ-ONLY VIEWS
# ------------------------
class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    List all books. Public view.
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
    Retrieve a single book. Public view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# ------------------------
# AUTHENTICATED CRUD VIEWS
# ------------------------
class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Create a book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /api/books/<id>/update/
    Update a book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # get book id from query parameter ?id=1
        pk = self.request.query_params.get("id")
        return generics.get_object_or_404(Book, pk=pk)

class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/<id>/delete/
    Delete a book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
