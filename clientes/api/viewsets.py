from rest_framework import viewsets

# models
from clientes.models import Cliente

# serializers
from clientes.api.serializers import ClienteSerialize

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerialize