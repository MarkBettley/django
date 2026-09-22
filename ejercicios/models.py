from django.conf import settings
from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    seller = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    product_dimensions = models.CharField(max_length=100)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="products",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
