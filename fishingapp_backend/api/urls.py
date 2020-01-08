"""
api/urls.py
"""
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    #---------------------------#
    # UNPROTECTED API ENDPOINTS #
    # --------------------------#

    # HOMEPAGE
    path('', views.UserLocationAPI.as_view(), name='UserLocationAPI' ),

    # pm
    path('api/fishingspots', views.FishingSpotListAPI.as_view(), name='FishingSpotListAPI'),
    path('api/searchelements', views.SearchElementListAPI.as_view(), name='SearchElementListAPI'),
    # path('api/favorites', views.FavoritesListAPI.as_view(), name='FavoritesListAPI'),

    # GATEWAY
    path('api/register', views.RegisterAPI.as_view(), name='register_api'),
    path('api/login', obtain_auth_token, name='api_token_auth'),

    #-------------------------#
    # PROTECTED API ENDPOINTS #
    #-------------------------#

    # DASHBOARD
    path('api/dashboard', views.DashboardAPI.as_view(), name='dashboard_api'),
    path('api/favourites', views.FavouritesAPI.as_view(), name='add_favourites'),

]
