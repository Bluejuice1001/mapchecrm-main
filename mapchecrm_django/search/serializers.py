from rest_framework import serializers

from .models import Search


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
      model = Search
      read_only_fields = (
        'id',
        'mapche_key',
        'formatted_address',
        'location_lat',
        'location_lng',
        'place_id',
        'address_component_nr',
        'address_component_street',
        'address_component_suburb',
        'address_component_town',
        'address_component_metro',
        'address_component_province',
        'address_component_province_short',
        'address_component_country',
        'address_component_country_short',
        'address_component_postal_code',
        'infoCity',
        'infoCountry',
        'infoIp',
        'infoLocation',
        'infoOrganization',
        'infoPostal_code',
        'infoRegion',
        'infoTimezone',
        'created_at',
        'modified_at',
      ),
      fields = (
        'id',
        'mapche_key',
        'formatted_address',
        'location_lat',
        'location_lng',
        'place_id',
        'address_component_nr',
        'address_component_street',
        'address_component_suburb',
        'address_component_town',
        'address_component_metro',
        'address_component_province',
        'address_component_province_short',
        'address_component_country',
        'address_component_country_short',
        'address_component_postal_code',
        'infoCity',
        'infoCountry',
        'infoIp',
        'infoLocation',
        'infoOrganization',
        'infoPostal_code',
        'infoRegion',
        'infoTimezone',
        'created_at',
        'modified_at',
       )

  