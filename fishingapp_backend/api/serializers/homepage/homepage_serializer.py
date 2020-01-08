from rest_framework import serializers
from django.contrib.auth.models import User


class UserLocationSerializer(serializers.Serializer):
    country = serializers.CharField(required=False)
    province = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
