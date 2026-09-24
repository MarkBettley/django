from rest_framework import serializers

from .models import ProductModel


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = [
            "id",
            "name",
            "price",
            "description",
            "seller",
            "color",
            "product_dimensions",
        ]
        read_only_fields = ["id"]
