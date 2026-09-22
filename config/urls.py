"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejercicios.views import (
    inicio,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProtectedListView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),

    path(
        'products/',
        ProductListView.as_view(),
        name='product-list'
    ),

    path(
        'products/create/',
        ProductCreateView.as_view(),
        name='product-create'
    ),

    path(
        'products/<int:pk>/',
        ProductDetailView.as_view(),
        name='product-detail'
    ),

    path(
        'products/<int:pk>/update/',
        ProductUpdateView.as_view(),
        name='product-update'
    ),

    path(
        'products/<int:pk>/delete/',
        ProductDeleteView.as_view(),
        name='product-delete'
    ),
    path(
        'my-products/',
        ProtectedListView.as_view(),
        name='my-products'
    ),
]
