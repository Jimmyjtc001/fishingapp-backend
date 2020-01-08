from django.http import HttpResponse, JsonResponse
from rest_framework import response, views, status
from rest_framework import generics

from foundation.models import UserLocation, FishingSpot, SearchElement,  Favorite
from api.serializers import FishingSpotSerializer, SearchElementSerializer, UserLocationSerializer


## CODE with the help of Daniel ##
## https://github.com/DanielSalazar1/fiftyoff-backend/blob/master/fifty_off/api/views/homepage/views.py

class UserLocationAPI(generics.ListAPIView):

    serializer_class = UserLocationSerializer

    def get_queryset(self):
        user_location = self.request.query_params.get('country', 'province', 'city', None)

        queryset = UserLocation.objects.filter(user=self.request.user)

        if attribute_name is not None:
            queryset = queryset.filter(user_location=user_location) # (location = self.request.(city, province, country))
            return queryset
