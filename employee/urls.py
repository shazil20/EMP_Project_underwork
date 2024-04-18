from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet
from . import views

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('createuser/', views.createuser, name='createuser'),
]
