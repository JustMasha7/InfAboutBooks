from django.urls import path
from . import views
from rest_framework import routers
from .api import BookViewSet

router = routers.DefaultRouter()
router.register('api/book', BookViewSet, 'book')
#router.register('api/author', AuthorViewSet, 'author')
urlpatterns = router.urls

urlpatterns = {
	path('', views.user, name = 'user')
    }
