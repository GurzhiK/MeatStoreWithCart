from django.shortcuts import render
from .models import Category
from .serializers import CategoryListSerializer, CategoryDetailSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class CategoryCreate(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryUpdate(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDelete(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
