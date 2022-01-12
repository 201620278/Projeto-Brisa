from django.db import models

from clientes.models import Cliente
from enderecos.models import Endereco


class Ponto(models.Model):
    data_criacao = models.DateTimeField('Data de criação', auto_now_add=True)
    data_atualizacao = models.DateTimeField('Data de atualização', auto_now=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=False)
    data_remocao = models.DateTimeField(auto_now=True)
