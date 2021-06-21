from django.shortcuts import render
from .models import Author, Book 

def user(request):
    all_author_list = Author.objects.all()
    return render(request, 'InfBooks/list.html',{'all_author_list':all_author_list})
