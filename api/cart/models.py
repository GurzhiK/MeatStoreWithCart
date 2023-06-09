from django.db import models
from accounts.models import UserAccount
from api.product.models import Product


class Cart(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart for {self.user.email}"


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart Item: {self.product.title}"
