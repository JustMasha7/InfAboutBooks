from django.http import HttpResponse

from django.shortcuts import render
from .models import Author, Book
from django.views import generic
#from rest_framework import generics
#from .serializers import BookSerializer, AuthorSerializer

def user(request):
    all_author_list = Author.objects.all()
    all_book_list = Book.objects.all()
    return render(request, 'InfBooks/list.html',{'all_author_list':all_author_list, 'all_book_list':all_book_list})
