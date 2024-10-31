from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'cost', 'amount', 'description', 'note', 'add_time', 'status', 'category']
