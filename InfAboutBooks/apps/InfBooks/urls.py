from django.urls import path, include
from . import views
from rest_framework import routers
from .api import BookViewSet, AuthorViewSet
from .views import *


app_name = 'Book'
urlpatterns = {
	path('', views.user, name = 'user'),
	#path('book/create/', BookCreateView.as_view()),
    }
#router = routers.DefaultRouter()
#router.register('api/book', BookViewSet, 'book')
#router.register('api/author', AuthorViewSet, 'author')
#urlpatterns = router.urls
