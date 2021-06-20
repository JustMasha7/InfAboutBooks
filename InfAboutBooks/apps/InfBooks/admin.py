from django.contrib import admin
#from django.db.models import Count
from django.db import models
from .models import Author, Book
#from itertools import chain


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name')
    list_display_links = ('id','author_name')
    search_fields = ('id', 'author_name')
    list_filter = ('author_name',)

class BooksAdmin(admin.ModelAdmin):
    #def author_names(self, obj):
    #    a = obj.authors.values('author_name')
    #    return list(chain.from_iterable(a))
    list_display = ('id', 'book_title')
    list_display_links = ('id','book_title')
    search_fields = ('id', 'book_title')
    list_filter = ('date_issue','date_return')

admin.site.register(Book,BooksAdmin)
admin.site.register(Author,AuthorAdmin)
