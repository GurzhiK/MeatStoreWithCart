from django.db import models
from accounts.models import UserAccount
from api.product.models import Product


class Cart(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart for {self.user.email}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"Cart Item: {self.product.title}"
