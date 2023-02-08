from django.db import router
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UserProfileViewSet

router = DefaultRouter()
router.register('userprofile', UserProfileViewSet, basename='userprofile')

urlpatterns = [
  path('', include(router.urls)),
]
