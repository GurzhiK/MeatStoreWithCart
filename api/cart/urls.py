from django.urls import path
from .views import CartItemsView

urlpatterns = [
    path('cart/items/', CartItemsView.as_view(), name='cart-items'),
    path('cart/items/<int:pk>/', CartItemsView.as_view(), name='cart-item-detail'),
]
