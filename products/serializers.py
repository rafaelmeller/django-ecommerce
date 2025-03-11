from rest_framework import serializers
from .models import Product, ProductVariation

class ProductVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariation
        fields = ['id', 'variation_type', 'value', 'stock']

class ProductSerializer(serializers.ModelSerializer):
    variations = ProductVariationSerializer(many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.username')


    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'created_at', 'variations', 'user']
