from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('books/',include('InfBooks.urls')),
    path('admin/', admin.site.urls),
]
