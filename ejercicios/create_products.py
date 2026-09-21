from .models import ProductModel


def create_products():
    products = []

    for i in range(1, 501):
        product = ProductModel(
            name=f"Producto {i}",
            price=100 + i,
            description=f"Descripción del producto de prueba {i}",
            seller=f"Vendedor {(i % 10) + 1}",
            color=f"Color {(i % 5) + 1}",
            product_dimensions=f"{10 + (i % 20)} x {20 + (i % 20)} x 5 cm",
        )

        products.append(product)

    ProductModel.objects.bulk_create(products)

    print(f"Productos creados: {ProductModel.objects.count()}")
