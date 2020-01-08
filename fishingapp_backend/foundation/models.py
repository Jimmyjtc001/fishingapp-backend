import uuid
from django.db import models
from django.contrib.auth.models import User

class UserLocation(models.Model):
    country = models.CharField(max_length=70)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class FishingSpot(models.Model):
    name = models.CharField(max_length=200)
    is_hidden = models.BooleanField(default=False, blank=True,)

    def __str__(self):
        return self.name


class SearchElement(models.Model):
    fishingSpot = models.ForeignKey(
        FishingSpot,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    type_of_fishing_found = models.CharField(max_length=255, blank=True, null=True,)
    kind_of_fishing_gear_to_bring = models.CharField(max_length=255, blank=True, null=True,)
    adress = models.CharField(max_length=255, blank=True, null=True,)
    country = models.CharField(max_length=255,)
    province = models.CharField(max_length=255, blank=True, null=True,)
    city = models.CharField(max_length=255,)
    is_hidden = models.BooleanField(default=False, blank=True,)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    searchelement = models.ForeignKey(
        SearchElement,
        on_delete=models.CASCADE
    )
