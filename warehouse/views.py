from django.shortcuts import render
from rest_framework import generics
from .models import Warehouse
from .serializers import ShopSerializer




class ShopDetailAPIView(generics.RetrieveAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = ShopSerializer
    lookup_field = 'pk'

