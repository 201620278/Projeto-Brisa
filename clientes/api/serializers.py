from rest_framework import serializers

# models
from clientes.models import Cliente

class ClienteSerialize(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nome', 'tipo')
