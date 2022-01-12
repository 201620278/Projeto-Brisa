from rest_framework import viewsets

# models

from ponto.models import Ponto

# serializers

from ponto.api.serializers import PontoSerialize


class PontoViewSet(viewsets.ModelViewSet):
    queryset = Ponto.objects.all()
    serializer_class = PontoSerialize
