# Generated by Django 3.0.10 on 2021-02-16 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_de_datos_prueba', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='vendedores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('fecha_alta', models.DateField()),
            ],
        ),
    ]
