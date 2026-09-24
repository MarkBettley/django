from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 10
    page_query_param = "pagina"
    page_size_query_param = "por_pagina"
    max_page_size = 50
