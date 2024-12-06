# Generated by Django 5.1.1 on 2024-09-27 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicativo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('duracao', models.CharField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]