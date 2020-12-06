from rest_framework import viewsets

from apps.questoes.api.serializers import QuestoesSerializer
from apps.questoes.models import Questoes


class QuestoesViewSet(viewsets.ModelViewSet):
    queryset = Questoes.objects.all()
    serializer_class = QuestoesSerializer

