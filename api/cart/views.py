from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CartItems, Cart
from api.product.models import Product
from .serializers import CartItemsSerializer
from rest_framework.permissions import IsAuthenticated


class CartItemsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart_items = CartItems.objects.filter(cart__user=request.user)
        serializer = CartItemsSerializer(cart_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CartItemsSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product']
            quantity = serializer.validated_data['quantity']
            try:
                product = Product.objects.get(id=product_id)
                if product.stock >= quantity:
                    cart = Cart.objects.get(user=request.user)
                    serializer.save(cart=cart)
                    product.stock -= quantity
                    product.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': 'Not enough stock available'}, status=status.HTTP_400_BAD_REQUEST)
            except Product.DoesNotExist:
                return Response({'error': 'Product does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cart_item = CartItems.objects.get(pk=pk)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        cart_item = CartItems.objects.get(pk=pk)
        serializer = CartItemsSerializer(cart_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
