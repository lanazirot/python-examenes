# Generated by Django 4.1.2 on 2022-10-31 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('puesto', models.CharField(max_length=255)),
                ('correoElectronico', models.CharField(max_length=255)),
            ],
        ),
    ]
