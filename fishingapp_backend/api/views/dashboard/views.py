from django.http import HttpResponse, JsonResponse
from rest_framework import response, views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

from foundation.models import FishingSpot, SearchElement, Favorite
# from api.serializers import DashboardSerializer

class DashboardAPI(views.APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        new_pm = pm.objects.create(user=request.user)
        # serializer = DashboardSerializer(new_pm)
        return response.Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

## DO a LIST view

class FavouritesAPI(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        queryset = Favorite.objects.filter(user=self.request.user)

        return queryset


    def post(self, request):
        serializer = FavouriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True),
        serializer.save(),

        return response.Response(
            status = status.HTTP_201_CREATED,
        );
