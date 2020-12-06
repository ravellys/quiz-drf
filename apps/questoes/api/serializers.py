from rest_framework import serializers

from apps.questoes.models import Questoes


class QuestoesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questoes
        fields = '__all__'
