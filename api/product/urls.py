from django.contrib import admin
from django.urls import path
from .views import ProductList, ProductDetail, ProductCreate, ProductDelete, ProductUpdate

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/detail/<int:pk>/',
         ProductDetail.as_view(), name='product-detail'),
    path('products/create/',
         ProductCreate.as_view(), name='product-create'),
    path('products/delete/<int:pk>/',
         ProductDelete.as_view(), name='product-delete'),
    path('products/update/<int:pk>/',
         ProductUpdate.as_view(), name='product-update'),
]
