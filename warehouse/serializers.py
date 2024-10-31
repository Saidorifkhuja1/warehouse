
from rest_framework import serializers
from .models import Warehouse

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'name', 'owner', 'address', 'phone_number', 'description']
