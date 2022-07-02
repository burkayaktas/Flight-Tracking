from webbrowser import get
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from flight.serializers import FlightSerializer, AirportSerializer
from flight.models import Airport, Flight
from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK


class AirportViewSets(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = []
    
 
    
    
class FlightViewSets(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = []
    
    @action(detail=True, methods=["get"])
    def flight_number(self, request, *args, **kwargs):
        qs = Flight.objects.filter(flight_number=request.query_params.get("flight_number")).count() 
        print(qs)
        return Response({"count":qs, "flight_number": request.query_params.get("flight_number")})  
    
    
