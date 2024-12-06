# Generated by Django 5.1.1 on 2024-11-08 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicativo', '0002_curso'),
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
        migrations.AddField(
            model_name='curso',
            name='imagem',
            field=models.ImageField(null=True, upload_to='imagens/courses/'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='imagem',
            field=models.ImageField(null=True, upload_to='imagens/users/'),
        ),
    ]
