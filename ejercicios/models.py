from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    seller = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    product_dimensions = models.CharField(max_length=100)

    def __str__(self):
        return self.name
# Create your models here.
