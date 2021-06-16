from django.http import HttpResponse

from django.shortcuts import render
from .models import Author, Book
from django.views import generic

def user(request):
    all_author_list = Author.objects.order_by('author_name')
    return render(request, 'InfBooks/list.html',{'all_author_list':all_author_list})
class BookListView(generic.ListView):
    model = Book
    context_object_name = 'all_book_list'
