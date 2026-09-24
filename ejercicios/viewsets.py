from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import ProductModel
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all().order_by("id")
    serializer_class = ProductSerializer

    # CREATE - Crear
    def create(self, request, *args, **kwargs):
        print("ViewSet CREATE ejecutado")

        serializer = self.get_serializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    # LIST - Listar
    def list(self, request, *args, **kwargs):
        print("ViewSet LIST ejecutado")

        queryset = self.filter_queryset(
            self.get_queryset()
        )

        serializer = self.get_serializer(
            queryset,
            many=True,
        )

        return Response(serializer.data)

    # RETRIEVE - Consultar
    def retrieve(self, request, *args, **kwargs):
        print("ViewSet RETRIEVE ejecutado")

        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)

    # UPDATE - Actualizar completamente
    def update(self, request, *args, **kwargs):
        print("ViewSet UPDATE ejecutado")

        partial = kwargs.pop("partial", False)
        instance = self.get_object()

        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial,
        )

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    # PARTIAL_UPDATE - Actualizar parcialmente
    def partial_update(
        self,
        request,
        *args,
        **kwargs,
    ):
        print("ViewSet PARTIAL_UPDATE ejecutado")

        kwargs["partial"] = True

        return self.update(
            request,
            *args,
            **kwargs,
        )

    # DESTROY - Borrar
    def destroy(self, request, *args, **kwargs):
        print("ViewSet DESTROY ejecutado")

        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(
            {
                "message":
                "Producto eliminado correctamente"
            },
            status=status.HTTP_200_OK,
        )
