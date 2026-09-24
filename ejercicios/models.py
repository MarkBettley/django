from django.conf import settings
from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    description = models.TextField()
    seller = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    product_dimensions = models.CharField(
        max_length=100
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="products",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class SaleModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sales",
    )

    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name="sales",
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    sale_date = models.DateTimeField(
        auto_now_add=True
    )

    @property
    def total(self):
        if self.unit_price is None:
            return 0

        return (
            self.quantity
            * self.unit_price
        )

    def __str__(self):
        return (
            f"Venta #{self.id} - "
            f"{self.product.name}"
        )
