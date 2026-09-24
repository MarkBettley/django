"""
URL configuration for config project.
"""

from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from ejercicios.api import products_api
from ejercicios.profile_api import UserProfileView
from ejercicios.viewsets import ProductViewSet
from ejercicios.views import (
    inicio,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProtectedListView,
    register,
)


router = DefaultRouter()
router.register(
    "products",
    ProductViewSet,
    basename="viewset-products",
)


urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),

    path(
        "",
        inicio,
        name="inicio",
    ),

    path(
        "products/",
        ProductListView.as_view(),
        name="product-list",
    ),

    path(
        "products/create/",
        ProductCreateView.as_view(),
        name="product-create",
    ),

    path(
        "products/<int:pk>/",
        ProductDetailView.as_view(),
        name="product-detail",
    ),

    path(
        "products/<int:pk>/update/",
        ProductUpdateView.as_view(),
        name="product-update",
    ),

    path(
        "products/<int:pk>/delete/",
        ProductDeleteView.as_view(),
        name="product-delete",
    ),

    path(
        "my-products/",
        ProtectedListView.as_view(),
        name="my-products",
    ),

    path(
        "register/",
        register,
        name="register",
    ),

    path(
        "accounts/login/",
        LoginView.as_view(
            template_name="ejercicios/login.html"
        ),
        name="login",
    ),

    # API REST del ejercicio anterior
    path(
        "api/products/",
        products_api,
        name="api-products",
    ),

    path(
        "api/products/<int:product_id>/",
        products_api,
        name="api-product-detail",
    ),

    # Django REST Framework ViewSet
    path(
        "api/viewset/",
        include(router.urls),
    ),

    # Autenticación con Token
    path(
        "api/token/",
        obtain_auth_token,
        name="api-token",
    ),

    # Perfil del usuario autenticado
    path(
        "api/profile/",
        UserProfileView.as_view(),
        name="api-profile",
    ),
]
