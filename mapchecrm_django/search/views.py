from django.shortcuts import render

# Create your views here. call below allows deleting, updating and retrieving

from rest_framework import viewsets

from userprofile.models import UserProfile

from .models import Search
from .serializers import SearchSerializer


class SearchViewSet(viewsets.ModelViewSet):
  serializer_class = SearchSerializer
#  queryset = Search.objects.all()
  queryset = Search.objects.filter()

  def get_queryset(self):
    if self.request.user.is_superuser:    #always add for superuser to view everything
      return self.queryset
    elif self.request.user.is_active:
      watchlist_id = UserProfile.objects.filter(user_id = self.request.user).values('mapche_key') 
      return self.queryset.filter(mapche_key__in=watchlist_id).all()

  def perform_create(self, serializer):
    serializer.save(created_by=self.request.user)

