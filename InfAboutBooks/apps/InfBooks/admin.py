from django.contrib import admin

from .models import Author, Book


class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_title')
    list_display_links = ('id','book_title')
    search_fields = ('id', 'book_title')
    list_filter = ('date_issue','date_return')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name')
    list_display_links = ('id','author_name')
    search_fields = ('id', 'author_name')
    list_filter = ('author_name',)


admin.site.register(Book,BooksAdmin)
admin.site.register(Author,AuthorAdmin)
