from rest_framework import serializers
from .models import CartItems


class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = ['id', 'product', 'quantity']
        extra_kwargs = {
            'cart': {'required': False}  # Make the cart field optional
        }
