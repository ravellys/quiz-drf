from rest_framework import serializers

from apps.categorias.models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ('nome', )
