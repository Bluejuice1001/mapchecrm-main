from django.contrib.auth.models import User
from django.db import models

class Search(models.Model):
  mapche_key = models.CharField(max_length=36, blank=True, null=True)
  formatted_address = models.CharField(max_length=255)
  location_lat = models.FloatField()
  location_lng = models.FloatField()
  place_id = models.CharField(max_length=255)
  address_component_nr = models.CharField(max_length=6, blank=True, null=True)
  address_component_street = models.CharField(max_length=85, blank=True, null=True)
  address_component_suburb = models.CharField(max_length=58, blank=True, null=True)
  address_component_town = models.CharField(max_length=58, blank=True, null=True)
  address_component_metro = models.CharField(max_length=255, blank=True, null=True)
  address_component_province = models.CharField(max_length=58, blank=True, null=True)
  address_component_province_short = models.CharField(max_length=4, blank=True, null=True)
  address_component_country = models.CharField(max_length=58, blank=True, null=True)
  address_component_country_short = models.CharField(max_length=4, blank=True, null=True)
  address_component_postal_code = models.CharField(max_length=8, blank=True, null=True)
  infoCity = models.CharField(max_length=255, blank=True, null=True)
  infoCountry = models.CharField(max_length=255, blank=True, null=True)
  infoIp = models.CharField(max_length=255, blank=True, null=True)
  infoLocation = models.CharField(max_length=255, blank=True, null=True)
  infoOrganization = models.CharField(max_length=255, blank=True, null=True)
  infoPostal_code = models.CharField(max_length=8, blank=True, null=True)
  infoRegion = models.CharField(max_length=58, blank=True, null=True)
  infoTimezone = models.CharField(max_length=255, blank=True, null=True)
  created_by = models.ForeignKey(User, related_name='searches', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)


