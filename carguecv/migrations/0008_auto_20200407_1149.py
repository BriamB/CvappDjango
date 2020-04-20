# Generated by Django 3.0.4 on 2020-04-07 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carguecv', '0007_auto_20200402_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carga_cv',
            name='experiencia_profesional',
        ),
        migrations.RemoveField(
            model_name='carga_cv',
            name='formacion',
        ),
        migrations.AlterField(
            model_name='carga_cv',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carguecv.Cargo'),
        ),
    ]