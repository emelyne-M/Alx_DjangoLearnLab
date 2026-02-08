from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):

    def setUp(self):
        """
        Runs before every test
        """
        # Create user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        # Create author
        self.author = Author.objects.create(name="George Orwell")

        # Create books
        self.book1 = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )

        self.book2 = Book.objects.create(
            title="Animal Farm",
            publication_year=1945,
            author=self.author
        )

    # ---------------- READ TESTS ----------------

    def test_list_books(self):
        """Anyone can view book list"""
        url = reverse("book-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        """Anyone can retrieve a single book"""
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "1984")

    # ---------------- CREATE TESTS ----------------

    def test_create_book_authenticated(self):
        """Authenticated user can create a book"""
        self.client.login(username="testuser", password="testpassword")

        url = reverse("book-create")
        data = {
            "title": "Homage to Catalonia",
            "publication_year": 1938,
            "author": self.author.id
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create a book"""
        url = reverse("book-create")
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2024,
            "author": self.author.id
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    # ---------------- UPDATE TESTS ----------------

    def test_update_book_authenticated(self):
        """Authenticated user can update a book"""
        self.client.login(username="testuser", password="testpassword")

        url = reverse("book-update", args=[self.book1.id])
        data = {
            "title": "Nineteen Eighty-Four",
            "publication_year": 1949,
            "author": self.author.id
        }

        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Nineteen Eighty-Four")

    # ---------------- DELETE TESTS ----------------

    def test_delete_book_authenticated(self):
        """Authenticated user can delete a book"""
        self.client.login(username="testuser", password="testpassword")

        url = reverse("book-delete", args=[self.book2.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ---------------- FILTER / SEARCH / ORDER ----------------

    def test_search_books(self):
        """Search by title"""
        url = reverse("book-list") + "?search=Animal"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_year(self):
        """Order books by publication_year"""
        url = reverse("book-list") + "?ordering=publication_year"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Animal Farm")

    def test_filter_books_by_year(self):
        """Filter books by publication_year"""
        url = reverse("book-list") + "?publication_year=1949"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
