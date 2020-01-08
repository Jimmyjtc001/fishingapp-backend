from rest_framework import serializers
from django.db import models

class FavoritesSerializer(serializers.Serializer):

        name = serializers.CharField()
        type_of_fishing_found = models.CharField()
        kind_of_fishing_gear_to_bring = models.CharField()
        adress = models.CharField()
        country = models.CharField()
        province = models.CharField()
        city = models.CharField()
        is_hidden = models.BooleanField()
