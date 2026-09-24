from django.contrib import admin

from .models import (
    ProductModel,
    SaleModel,
)


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
        "seller",
        "color",
        "user",
    )

    search_fields = (
        "name",
        "seller",
    )

    list_filter = (
        "color",
    )


@admin.register(SaleModel)
class SaleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "user",
        "quantity",
        "unit_price",
        "sale_date",
        "total",
    )

    search_fields = (
        "product__name",
        "user__username",
    )

    list_filter = (
        "sale_date",
    )

    readonly_fields = (
        "sale_date",
        "total",
    )
