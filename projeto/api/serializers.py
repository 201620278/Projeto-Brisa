from rest_framework import serializers

from ponto.models import Ponto


class PontoSerialize(serializers.ModelSerializer):
    class Meta:
        model = Ponto
        fields = ('cliente', 'enderecos')
