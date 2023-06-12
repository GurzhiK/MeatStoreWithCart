from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CartItems, Cart
from api.product.models import Product
from .serializers import CartItemsSerializer
from rest_framework.exceptions import ValidationError
from decimal import Decimal
from django.db import transaction
from rest_framework.permissions import IsAuthenticated


class CartItemsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart_items = CartItems.objects.filter(cart__user=request.user)
        serializer = CartItemsSerializer(cart_items, many=True)

        # Calculate total quantity and total amount
        total_quantity = sum(item.quantity for item in cart_items)
        total_amount = sum(item.product.price *
                           item.quantity for item in cart_items)

        data = {
            'cart_items': serializer.data,
            'total_quantity': total_quantity,
            'total_amount': total_amount,
        }

        return Response(data)

    def post(self, request):
        serializer = CartItemsSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product'].id
            quantity = serializer.validated_data['quantity']
            try:
                product = Product.objects.get(id=product_id)
                if product.stock >= quantity:
                    cart = Cart.objects.get(user=request.user)
                    serializer.save(cart=cart)
                    product.stock -= quantity
                    product.save()

                    # Calculate subtotal
                    subtotal = Decimal(quantity) * product.price

                    # Add subtotal to serializer data
                    data = serializer.data
                    data['subtotal'] = str(subtotal)

                    return Response(data, status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': 'Not enough stock available'}, status=status.HTTP_400_BAD_REQUEST)
            except Product.DoesNotExist:
                return Response({'error': 'Product does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            except Cart.DoesNotExist:
                raise ValidationError(
                    'Cart does not exist for the current user')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def delete(self, request, pk):
        try:
            cart_item = CartItems.objects.select_for_update().get(
                pk=pk)  # Lock the cart item for update
            product = cart_item.product
            quantity = cart_item.quantity
            cart_item.delete()

            # Return quantity to stock
            product.stock += quantity
            product.save()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except CartItems.DoesNotExist:
            return Response({'error': 'Cart item does not exist'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        cart_item = CartItems.objects.get(pk=pk)
        serializer = CartItemsSerializer(cart_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
