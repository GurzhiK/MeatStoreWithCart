from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class CartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = CartItemSerializer(data=request.data)

        if serializer.is_valid():
            item = serializer.save(cart=cart)
            product = item.product

            if product.stock == 0:
                item.delete()
                return Response({"error": "Product is out of stock."}, status=status.HTTP_400_BAD_REQUEST)

            if item.quantity > product.stock:
                item.delete()
                return Response({"error": "Cannot add more items than available in stock."}, status=status.HTTP_400_BAD_REQUEST)

            remaining_stock = product.stock - item.quantity

            if remaining_stock < 0:
                item.delete()
                return Response({"error": "Not enough stock available."}, status=status.HTTP_400_BAD_REQUEST)

            product.stock = remaining_stock
            product.save()

            serializer = CartItemSerializer(item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_id):
        cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
        product = cart_item.product
        product.stock += cart_item.quantity
        product.save()
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
