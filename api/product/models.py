from django.db import models
from api.category.models import Category


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    imageUrl = models.ImageField(upload_to='images/')
    stock = models.IntegerField()

    def __str__(self):
        return self.title
