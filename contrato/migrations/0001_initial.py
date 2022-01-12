# Generated by Django 4.0.1 on 2022-01-12 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ponto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('data_atualizacao', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('estado', models.CharField(choices=[('Em vigor', 'Em vigor'), ('Desativado Temporario', 'Desativado Temporario'), ('Cancelado', 'Cancelado')], max_length=128)),
                ('data_remocao', models.DateTimeField(auto_now=True)),
                ('ponto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ponto.ponto')),
            ],
        ),
        migrations.CreateModel(
            name='ContratoEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('data_atualizacao', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('estado_anterior', models.CharField(choices=[('Em vigor', 'Em vigor'), ('Desativado Temporario', 'Desativado Temporario'), ('Cancelado', 'Cancelado')], max_length=128)),
                ('estado_posterior', models.CharField(choices=[('Em vigor', 'Em vigor'), ('Desativado Temporario', 'Desativado Temporario'), ('Cancelado', 'Cancelado')], max_length=128)),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contrato.contrato')),
            ],
        ),
    ]