from django.contrib import admin
from .models import Book

# Register Book model with admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns in admin list
    list_filter = ('publication_year', 'author')            # filters
    search_fields = ('title', 'author')                     # search box
