from django.http import HttpResponse


class Producto:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def calcular_total(self, cantidad):
        return cantidad * self.precio


class ProductoInternacional(Producto):
    def __init__(self, nombre, precio, descripcion, tasa_internacional):
        super().__init__(nombre, precio, descripcion)
        self.tasa_internacional = tasa_internacional

    def calcular_total_con_tasa(self, cantidad):
        return self.calcular_total(cantidad) * (1 + self.tasa_internacional)


# Ejemplos de instanciación de objetos
producto = Producto(
    "Camiseta",
    50.0,
    "Camiseta de algodón"
)

producto_internacional = ProductoInternacional(
    "Tenis",
    100.0,
    "Tenis deportivos importados",
    0.16
)


def inicio(request):
    return HttpResponse(
        f"<h1>Fundamentos de Linux e Introducción a Django</h1>"
        f"<h2>Producto nacional</h2>"
        f"<p>Nombre: {producto.nombre}</p>"
        f"<p>Precio: ${producto.precio}</p>"
        f"<p>Descripción: {producto.descripcion}</p>"
        f"<p>Total por 10 unidades: ${producto.calcular_total(10)}</p>"
        f"<h2>Producto internacional</h2>"
        f"<p>Nombre: {producto_internacional.nombre}</p>"
        f"<p>Precio: ${producto_internacional.precio}</p>"
        f"<p>Descripción: {producto_internacional.descripcion}</p>"
        f"<p>Tasa internacional: {producto_internacional.tasa_internacional}</p>"
        f"<p>Total con tasa por 10 unidades: "
        f"${producto_internacional.calcular_total_con_tasa(10)}</p>"
    )
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import ProductModel


class ProductListView(ListView):
    model = ProductModel
    template_name = "ejercicios/product_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = "ejercicios/product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = ProductModel
    fields = [
        "name",
        "price",
        "description",
        "seller",
        "color",
        "product_dimensions",
    ]
    template_name = "ejercicios/product_form.html"
    success_url = reverse_lazy("product-list")


class ProductUpdateView(UpdateView):
    model = ProductModel
    fields = [
        "name",
        "price",
        "description",
        "seller",
        "color",
        "product_dimensions",
    ]
    template_name = "ejercicios/product_form.html"
    success_url = reverse_lazy("product-list")


class ProductDeleteView(DeleteView):
    model = ProductModel
    template_name = "ejercicios/product_confirm_delete.html"
    success_url = reverse_lazy("product-list")


from django.contrib.auth.mixins import LoginRequiredMixin


class ProtectedListView(LoginRequiredMixin, ListView):
    model = ProductModel
    template_name = "ejercicios/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        return ProductModel.objects.filter(user=self.request.user)


from django.shortcuts import redirect, render

from .forms import UserRegistrationForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserRegistrationForm()

    return render(
        request,
        "ejercicios/register.html",
        {"form": form},
    )
