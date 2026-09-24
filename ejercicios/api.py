import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import ProductModel


@csrf_exempt
def products_api(request, product_id=None):

    # GET - Consultar o listar productos
    if request.method == "GET":
        print("Método GET ejecutado")

        if product_id is not None:
            try:
                product = ProductModel.objects.get(pk=product_id)
            except ProductModel.DoesNotExist:
                return JsonResponse(
                    {"error": "Producto no encontrado"},
                    status=404,
                )

            data = {
                "id": product.id,
                "name": product.name,
                "price": str(product.price),
                "description": product.description,
                "seller": product.seller,
                "color": product.color,
                "product_dimensions": product.product_dimensions,
            }

            return JsonResponse(data)

        products = list(
            ProductModel.objects.values(
                "id",
                "name",
                "price",
                "description",
                "seller",
                "color",
                "product_dimensions",
            )
        )

        return JsonResponse(
            {"products": products}
        )

    # POST - Crear un producto
    if request.method == "POST":
        print("Método POST ejecutado")

        try:
            data = json.loads(request.body)

            product = ProductModel.objects.create(
                name=data["name"],
                price=data["price"],
                description=data["description"],
                seller=data["seller"],
                color=data["color"],
                product_dimensions=data["product_dimensions"],
            )

            return JsonResponse(
                {
                    "message": "Producto creado correctamente",
                    "id": product.id,
                },
                status=201,
            )

        except (json.JSONDecodeError, KeyError):
            return JsonResponse(
                {"error": "Datos inválidos"},
                status=400,
            )

    # PUT - Actualizar un producto
    if request.method == "PUT":
        print("Método PUT ejecutado")

        if product_id is None:
            return JsonResponse(
                {"error": "Debes indicar el ID del producto"},
                status=400,
            )

        try:
            product = ProductModel.objects.get(pk=product_id)
        except ProductModel.DoesNotExist:
            return JsonResponse(
                {"error": "Producto no encontrado"},
                status=404,
            )

        try:
            data = json.loads(request.body)

            product.name = data.get("name", product.name)
            product.price = data.get("price", product.price)
            product.description = data.get(
                "description",
                product.description,
            )
            product.seller = data.get(
                "seller",
                product.seller,
            )
            product.color = data.get(
                "color",
                product.color,
            )
            product.product_dimensions = data.get(
                "product_dimensions",
                product.product_dimensions,
            )

            product.save()

            return JsonResponse(
                {
                    "message": "Producto actualizado correctamente",
                    "id": product.id,
                }
            )

        except json.JSONDecodeError:
            return JsonResponse(
                {"error": "JSON inválido"},
                status=400,
            )

    # DELETE - Eliminar un producto
    if request.method == "DELETE":
        print("Método DELETE ejecutado")

        if product_id is None:
            return JsonResponse(
                {"error": "Debes indicar el ID del producto"},
                status=400,
            )

        try:
            product = ProductModel.objects.get(pk=product_id)
        except ProductModel.DoesNotExist:
            return JsonResponse(
                {"error": "Producto no encontrado"},
                status=404,
            )

        product.delete()

        return JsonResponse(
            {"message": "Producto eliminado correctamente"}
        )

    return JsonResponse(
        {"error": "Método HTTP no permitido"},
        status=405,
    )
