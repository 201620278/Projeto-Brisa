from rest_framework import serializers

# models
from ponto.models import Ponto


class PontoSerialize(serializers.ModelSerializer):
    class Meta:
        model = Ponto
        fields = ('endereco','cliente','data_criacao','data_atualizacao')
