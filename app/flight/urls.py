from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('flight', views.FlightViewSets)
router.register('airport', views.AirportViewSets)



urlpatterns = [
    path('', include(router.urls)),
]