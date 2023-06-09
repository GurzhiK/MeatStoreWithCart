from django.shortcuts import render
from .models import Category
from .serializers import CategoryListSerializer, CategoryDetailSerializer
from rest_framework import generics


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class CategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryUpdate(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDelete(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
