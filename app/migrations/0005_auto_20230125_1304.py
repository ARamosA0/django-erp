# Generated by Django 3.2 on 2023-01-25 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_trabajador_borrado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden_compra_servicio',
            name='trabajador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.trabajador'),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='contratista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.trabajador'),
        ),
    ]
