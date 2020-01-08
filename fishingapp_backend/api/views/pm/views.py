from django.http import HttpResponse, JsonResponse
from rest_framework import response, views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

from foundation.models import UserLocation, FishingSpot, SearchElement, Favorite
from api.serializers import FishingSpotSerializer, SearchElementSerializer
from api.serializers import UserLocationSerializer
# FavoritesSerializer

class FishingSpotListAPI(generics.ListAPIView):
    serializer_class = FishingSpotSerializer

    def get_queryset(self):
        queryset = FishingSpot.objects.filter(is_hidden=False).order_by('name')

        return queryset

class SearchElementListAPI(generics.ListAPIView):

    serializer_class = SearchElementSerializer

    def get_queryset(self):
        queryset = pm.objects.filter(is_hidden=False).order_by('name')

        return queryset
