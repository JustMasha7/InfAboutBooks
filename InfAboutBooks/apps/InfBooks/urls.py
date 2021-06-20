from django.urls import path, include
from . import views
from rest_framework import routers
from .api import BookViewSet, AuthorViewSet 

router = routers.DefaultRouter()
router.register('api/book', BookViewSet, 'book')
router.register('api/author', AuthorViewSet, 'author')
urlpatterns = [
	path('list/', views.user, name = 'user'),
	path('', include(router.urls)),
    ]
