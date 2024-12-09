from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TagViewSet,TaskViewSet

router = DefaultRouter()
router.register('users',UserViewSet)
router.register('tasks',TaskViewSet)
router.register('tags',TagViewSet)

urlpatterns = [
    path('',include(router.urls))
]