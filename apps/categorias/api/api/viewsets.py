from rest_framework import viewsets

from apps.categorias.api.api.serializers import CategoriaSerializer
from apps.categorias.models import Categoria


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

