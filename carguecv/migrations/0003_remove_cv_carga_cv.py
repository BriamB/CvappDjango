# Generated by Django 3.0.4 on 2020-04-01 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carguecv', '0002_cargo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='carga_cv',
        ),
    ]