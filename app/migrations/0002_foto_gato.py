# Generated by Django 5.1.3 on 2024-11-29 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('imagem', models.ImageField(null=True, upload_to='imagens/')),
            ],
        ),
        migrations.CreateModel(
            name='Gato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('raca', models.CharField(max_length=100)),
                ('imagem', models.ImageField(null=True, upload_to='imagens/gatos/')),
            ],
        ),
    ]