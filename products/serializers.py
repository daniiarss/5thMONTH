from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = 'id title text price rating __str__'.split()
        # exclude = 'id'.split()
        # fields = ['id', 'title', 'rating']