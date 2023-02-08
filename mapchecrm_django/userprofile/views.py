from django.shortcuts import render

# Create your views here. call below allows deleting, updating and retrieving

from rest_framework import viewsets

from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
  serializer_class = UserProfileSerializer
  queryset = UserProfile.objects.all()

  def get_queryset(self):
    if self.request.user.is_superuser:    #always add for superuser to view everything
      return self.queryset
    elif self.request.user.is_active:
      return self.queryset.filter(user_id=self.request.user)
#    return self.queryset.filter(user_id = self.request.user).values('mapche_key') 

  def perform_create(self, serializer):
    serializer.save(user_id=self.request.user)
    
