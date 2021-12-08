from django.shortcuts import render

from rest_framework import generics
from .serializers import CarSerializer
from .models import Car

class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all().order_by('id') 
    serializer_class = CarSerializer

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all().order_by('id')
    serializer_class = CarSerializer

# Create your views here.
