from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import models
import uuid

class FavouriteSerializer(serializers.Serializer):
    name = models.CharField(max_length=255)
    serial = models.UUIDField(default=uuid.uuid4, editable=False)
    # photo = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True,)

    def create(self, validated_data):
        name = validated_data.get('name', None)
        serial = validated_data.get('serial', None)
        # photo = validated_data.get('photo')

        # Plug in our data from the request into our `User` model.
        new_item = item.objects.create(name = name, serial = serial)

        return new_item
