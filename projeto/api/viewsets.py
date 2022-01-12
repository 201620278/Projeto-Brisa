from rest_framework import viewsets

from ponto.api.serializers import PontoSerialize
from ponto.models import Ponto


class PontoViewSet(viewsets.ModelViewSet):
    queryset = Ponto.objects.all()
    serializer_class = PontoSerialize
