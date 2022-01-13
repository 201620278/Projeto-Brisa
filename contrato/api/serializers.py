from rest_framework import serializers

# models
from contrato.models import Contrato

class ContratoSerialize(serializers.ModelSerializer):
    cliente_id = serializers.CharField(source='ponto.cliente.id')
    cliente_nome = serializers.CharField(source='ponto.cliente.nome')
    cliente_tipo = serializers.CharField(source='ponto.cliente.tipo')
    endereco_id = serializers.CharField(source='ponto.endereco.id')
    endereco_logradouro = serializers.CharField(source='ponto.endereco.logradouro')
    endereco_bairro = serializers.CharField(source='ponto.endereco.bairro')
    endereco_numero = serializers.CharField(source='ponto.endereco.numero')
    class Meta:
        model = Contrato
        fields = ('id', 'cliente_id', 'cliente_nome', 'cliente_tipo', 'endereco_id', 'endereco_logradouro',
                  'endereco_bairro', 'endereco_numero')