from django.contrib import admin
from django.urls import path
from .views import CategoryList, CategoryDetail, CategoryCreate, CategoryDelete, CategoryUpdate

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/detail/<int:pk>/',
         CategoryDetail.as_view(), name='category-detail'),
    path('categories/create/',
         CategoryCreate.as_view(), name='category-create'),
    path('categories/delete/<int:pk>/',
         CategoryDelete.as_view(), name='category-delete'),
    path('categories/update/<int:pk>/',
         CategoryUpdate.as_view(), name='category-update'),
]
