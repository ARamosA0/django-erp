# Generated by Django 3.2 on 2023-01-23 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_produccion_produccion_linea'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura_clie',
            name='estadoprod',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
