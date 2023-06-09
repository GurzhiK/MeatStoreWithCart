from rest_framework import serializers
from .models import CartItems


class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = '__all__'
