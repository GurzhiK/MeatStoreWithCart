from rest_framework import serializers
from .models import Cart, CartItem, Product
from api.product.serializers import SimpleProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product',
                  'product_id', 'quantity', 'sub_total']
        extra_kwargs = {
            'cart': {'required': False}  # Make the cart field optional
        }


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'items', 'grand_total']

    def get_grand_total(self, obj):
        return sum(item.sub_total() for item in obj.items.all())
